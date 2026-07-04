"""Build a grouping instruction to run after query execution.

Usage:
    query = select(cliente).where(...).groupby(ClientModel.nome).execute()

If no explicit fields are passed, grouping is done by the selected fields
from the Select object.
"""

def groupby(*fields):
    from typing import Any
    from ORM_IXC.statemants.maps.classBase import Field

    def _groupby_instr(select_obj, results: list[Any]) -> None:

        fields_to_use = list(fields) if fields else select_obj.selected_fields
        if not fields_to_use:
            return None

        names: list[str] = []
        for f in fields_to_use:
            if isinstance(f, Field):
                names.append(f.name)
            elif hasattr(f, "name"):
                names.append(getattr(f, "name"))
            elif isinstance(f, str):
                names.append(f)

        if not names:
            return None

        seen: set = set()
        grouped: list = []
        for row in results:
            key = tuple(select_obj._raw_value(row, n) for n in names)
            if key not in seen:
                seen.add(key)
                grouped.append(row)

        results[:] = grouped
        try:
            select_obj._results = results
        except Exception:
            pass
        return None

    return _groupby_instr
