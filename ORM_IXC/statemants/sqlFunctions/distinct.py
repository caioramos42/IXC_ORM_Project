"""Mark a context for distinct filtering.

Usage:
    # distinct by selected fields (use .columns(...) on the Select)
    query = select(distinct(cliente)).where(...).execute()

    # or distinct by explicit fields
    query = select(distinct(cliente, ClientModel.nome)).where(...).execute()

This function attaches metadata to the context so the Select created
from it will append an instruction that filters duplicate rows after
the query is executed.
"""
def distinct(context, *fields):
    from typing import Any
    from ORM_IXC.statemants.maps.classBase import Field

    # register the function in a generic list so Select can discover it
    try:
        funcs = getattr(context, "_sql_functions", None)
        if funcs is None:
            funcs = []
            setattr(context, "_sql_functions", funcs)

        # build the distinct instruction as a callable capturing the fields
        def _distinct_instr(select_obj, results: list[Any]) -> None:
            # explicit fields passed to distinct() take precedence
            fields_to_use = list(fields) if fields else select_obj.selected_fields
            if not fields_to_use:
                return None

            # normalize to field names
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
            filtered: list = []
            for row in results:
                key = tuple(select_obj._raw_value(row, n) for n in names)
                if key not in seen:
                    seen.add(key)
                    filtered.append(row)

            results[:] = filtered
            select_obj._results = results
            return None

        funcs.append(_distinct_instr)
    except Exception:
        # best-effort: if context cannot be mutated, fall back to legacy attrs
        try:
            setattr(context, "_distinct_enabled", True)
            setattr(context, "_distinct_fields", list(fields))
        except Exception:
            pass
    return context