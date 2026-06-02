from ORM_IXC.interfaces.IModel import IModelWithId


def formatInner(itens: list[IModelWithId]) -> str:
    if len(itens) == 0:
        return ''
    innerList: str = ", ".join([str(iten.id) for iten in itens])
    return innerList



