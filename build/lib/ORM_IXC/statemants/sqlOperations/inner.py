# from typing import TypeVar
# from ORM_IXC.interfaces import IContext
# from ORM_IXC.interfaces.IModel import IModel
# from ORM_IXC.models.searchUtils.searchModel import SearchNode
# from ORM_IXC.statemants.CRUD.select import select

# T = TypeVar('T', bound=IModel)
# U = TypeVar('U', bound=IModel)


# def Inner(context: IContext[T, U], search: SearchNode, field: str, limit=500) -> str:
#     models = select(context).where(search).limit(limit).execute()
#     return *[model.field for model in models]
