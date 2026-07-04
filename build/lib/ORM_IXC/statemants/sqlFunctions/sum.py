"""Mark a context with a summation instruction for Select results.

Usage:
    query = select(sum(ctx, Model.value)).where(...).execute()
    query = select(sum(ctx, Model.value, "total")).where(...).groupby(...).execute()

If called with a field, returns the sum of that field (non-null values only).
Supports grouping: when grouped, returns one result per group with the alias set to the sum.
"""

def sum(context, field=None, alias: str = "sum"):
    from typing import Any
    import copy
    from ORM_IXC.statemants.maps.classBase import Field

    def _sum_instr(select_obj, results: list[Any]) -> None:
        if field is not None and isinstance(field, Field):
            sum_field_name = field.name
        elif field is not None and isinstance(field, str):
            sum_field_name = field
        else:
            sum_field_name = None

        group_fields = getattr(select_obj, "_group_fields", []) or []

        class SumResult:
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
            def dto_convert(cls, data: dict[str, str]) -> "SumResult":
                alias_name = "sum"
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
                    groups[key] = {"values": group_values, "sum": 0}

                if sum_field_name is None:
                    # no field specified -> cannot sum
                    continue
                else:
                    value = select_obj._raw_value(row, sum_field_name)
                    try:
                        v = float(value) if value not in (None, "") else 0
                    except Exception:
                        v = 0
                    groups[key]["sum"] += v

            grouped_results: list[Any] = []
            for group in groups.values():
                grouped_results.append(SumResult(group["values"], alias, group["sum"]))

            results[:] = grouped_results
            select_obj._results = results
            return None

        total_sum = 0
        for row in results:
            if sum_field_name is None:
                continue
            else:
                value = select_obj._raw_value(row, sum_field_name)
                try:
                    v = float(value) if value not in (None, "") else 0
                except Exception:
                    v = 0
                total_sum += v

        result_row = SumResult({}, alias, total_sum)
        results[:] = [result_row]
        select_obj._results = results
        return None

    funcs = getattr(context, "_sql_functions", None)
    if funcs is None:
        funcs = []
        setattr(context, "_sql_functions", funcs)
    funcs.append(_sum_instr)
    # expose alias field on context for comparisons in having
    try:
        from ORM_IXC.statemants.maps.classBase import Field as _Field
        sum_field = _Field(name=alias, fieldType=float)
        sum_field.model = getattr(context, "contextModel", None)
        try:
            setattr(context, alias, sum_field)
        except Exception:
            pass
    except Exception:
        pass

    setattr(context, "_sum_enabled", True)
    setattr(context, "_sum_field", field)
    setattr(context, "_sum_alias", alias)
    return context
