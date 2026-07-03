"""Mark a context with an average instruction for Select results.

Usage:
    query = select(avg(ctx, Model.value)).where(...).execute()
    query = select(avg(ctx, Model.value, "avg_val")).where(...).groupby(...).execute()

If called with a field, returns the average of that field (non-null values only).
Supports grouping: when grouped, returns one result per group with the alias set to the average.
"""

def avg(context, field=None, alias: str = "avg"):
    from typing import Any
    import copy
    from ORM_IXC.statemants.maps.classBase import Field

    def _avg_instr(select_obj, results: list[Any]) -> None:
        if field is not None and isinstance(field, Field):
            avg_field_name = field.name
        elif field is not None and isinstance(field, str):
            avg_field_name = field
        else:
            avg_field_name = None

        group_fields = getattr(select_obj, "_group_fields", []) or []

        class AvgResult:
            def __init__(self, values: dict[str, Any], alias_name: str, value: Any):
                self.alias = ""
                self.table = ""
                self._alias_name = alias_name
                for field_name, field_value in values.items():
                    setattr(self, field_name, field_value)
                setattr(self, alias_name, value)

            def output_dict(self) -> dict[str, str]:
                data: dict[str, str] = {}
                for key, val in vars(self).items():
                    if key in {"alias", "table", "_alias_name"}:
                        continue
                    if val is None:
                        data[key] = ""
                    else:
                        data[key] = str(val)
                return data

            def to_dict(self) -> dict[str, str]:
                return self.output_dict()

            @classmethod
            def dto_convert(cls, data: dict[str, str]) -> "AvgResult":
                alias_name = "avg"
                value = data.get(alias_name, 0)
                try:
                    value = float(value)
                except Exception:
                    pass
                return cls({}, alias_name, value)

            @classmethod
            def set_alias(cls_, alias: str):
                pass

        if group_fields:
            groups: dict[tuple, dict[str, Any]] = {}
            for row in results:
                key = tuple(select_obj._raw_value(row, n) for n in group_fields)
                if key not in groups:
                    group_values = {name: select_obj._raw_value(row, name) for name in group_fields}
                    groups[key] = {"values": group_values, "sum": 0, "count": 0}

                if avg_field_name is None:
                    continue
                else:
                    value = select_obj._raw_value(row, avg_field_name)
                    try:
                        v = float(value) if value not in (None, "") else 0
                    except Exception:
                        v = 0
                    groups[key]["sum"] += v
                    groups[key]["count"] += 1

            grouped_results: list[Any] = []
            for group in groups.values():
                avgv = (group["sum"] / group["count"]) if group["count"] > 0 else 0
                grouped_results.append(AvgResult(group["values"], alias, avgv))

            results[:] = grouped_results
            select_obj._results = results
            return None

        total_sum = 0
        total_count = 0
        for row in results:
            if avg_field_name is None:
                continue
            else:
                value = select_obj._raw_value(row, avg_field_name)
                try:
                    v = float(value) if value not in (None, "") else 0
                except Exception:
                    v = 0
                total_sum += v
                total_count += 1

        avg_value = (total_sum / total_count) if total_count > 0 else 0
        result_row = AvgResult({}, alias, avg_value)
        results[:] = [result_row]
        select_obj._results = results
        return None

    funcs = getattr(context, "_sql_functions", None)
    if funcs is None:
        funcs = []
        setattr(context, "_sql_functions", funcs)
    funcs.append(_avg_instr)
    # expose alias field on context to allow comparisons in having
    try:
        from ORM_IXC.statemants.maps.classBase import Field as _Field
        avg_field = _Field(name=alias, fieldType=float)
        avg_field.model = getattr(context, "contextModel", None)
        try:
            setattr(context, alias, avg_field)
        except Exception:
            pass
    except Exception:
        pass

    setattr(context, "_avg_enabled", True)
    setattr(context, "_avg_field", field)
    setattr(context, "_avg_alias", alias)
    return context
