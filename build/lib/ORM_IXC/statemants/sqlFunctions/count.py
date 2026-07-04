"""Mark a context with a counting instruction for Select results.

Usage:
    query = select(count(ctx)).where(...).execute()
    query = select(count(ctx, ClientModel.nome)).where(...).execute()
    query = select(count(ctx), groupby(ClientModel.nome)).where(...).execute()

If called without a field, returns the total number of rows.
If called with a field, counts non-null occurrences for that column.
"""

def count(context, field=None, alias: str = "count"):
    from typing import Any
    import copy
    from ORM_IXC.statemants.maps.classBase import Field

    def _count_instr(select_obj, results: list[Any]) -> None:
        if field is not None and isinstance(field, Field):
            count_field_name = field.name
        elif field is not None and isinstance(field, str):
            count_field_name = field
        else:
            count_field_name = None

        group_fields = getattr(select_obj, "_group_fields", []) or []

        class CountResult:
            def __init__(self, values: dict[str, Any], alias_name: str, value: int):
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
            def dto_convert(cls, data: dict[str, str]) -> "CountResult":
                alias_name = "count"
                value = int(data.get(alias_name, 0))
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
                    groups[key] = {"values": group_values, "count": 0}

                if count_field_name is None:
                    groups[key]["count"] += 1
                else:
                    value = select_obj._raw_value(row, count_field_name)
                    if value is not None and value != "":
                        groups[key]["count"] += 1

            grouped_results: list[Any] = []
            for group in groups.values():
                grouped_results.append(CountResult(group["values"], alias, group["count"]))

            results[:] = grouped_results
            select_obj._results = results
            return None

        total_count = 0
        for row in results:
            if count_field_name is None:
                total_count += 1
            else:
                value = select_obj._raw_value(row, count_field_name)
                if value is not None and value != "":
                    total_count += 1

        class CountResult:
            def __init__(self, alias_name: str, value: int):
                self.alias = ""
                self.table = ""
                self._alias_name = alias_name
                setattr(self, alias_name, value)

            def output_dict(self) -> dict[str, str]:
                if not hasattr(self, self._alias_name):
                    return {}
                return {self._alias_name: str(getattr(self, self._alias_name))}

            def to_dict(self) -> dict[str, str]:
                return self.output_dict()

            @classmethod
            def dto_convert(cls, data: dict[str, str]) -> "CountResult":
                alias_name = "count"
                value = int(data.get(alias_name, 0))
                return cls(alias_name, value)

            @classmethod
            def set_alias(cls_, alias: str):
                pass

        result_row = CountResult(alias, total_count)
        results[:] = [result_row]
        select_obj._results = results
        return None

    funcs = getattr(context, "_sql_functions", None)
    if funcs is None:
        funcs = []
        setattr(context, "_sql_functions", funcs)
    funcs.append(_count_instr)
    # expose an attribute on the context so it can be used in comparisons
    try:
        count_field = Field(name=alias, fieldType=int)
        count_field.model = getattr(context, "contextModel", None)
        try:
            setattr(context, alias, count_field)
        except Exception:
            pass
    except Exception:
        pass

    setattr(context, "_count_enabled", True)
    setattr(context, "_count_field", field)
    setattr(context, "_count_alias", alias)
    return context
