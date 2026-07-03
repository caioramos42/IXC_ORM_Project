from ORM_IXC.statemants.CRUD.select import select
from ORM_IXC.statemants.sqlFunctions.distinct import distinct
from ORM_IXC.statemants.maps.classBase import Field
from ORM_IXC.models.searchUtils.searchModel import SearchModule


class ClientModel:
    razao = Field(name="razao", fieldType=int)
    nome = Field(name="nome", fieldType=str)


ClientModel.razao.model = ClientModel
ClientModel.nome.model = ClientModel


class FakeRow:
    def __init__(self, razao: int, nome: str) -> None:
        self.razao = razao
        self.nome = nome
        self._inners: list[object] = []

    def inner(self, row: object) -> None:
        self._inners.append(row)


class FakeContext:
    def __init__(self, rows: list[FakeRow]) -> None:
        self.rows = rows
        self.contextModel = ClientModel

    def SelectByFilter(self, search: SearchModule) -> list[FakeRow]:
        if search.searchField == "razao":
            allowed = int(search.query)
            return [row for row in self.rows if getattr(row, "razao") == allowed]
        return []

    def SelectByFilterAssync(self, search: SearchModule, page_size: int):
        return iter(self.SelectByFilter(search))


def test_distinct_filters_duplicates():
    rows = [
        FakeRow(27560, "A"),
        FakeRow(27560, "A"),
        FakeRow(27560, "B"),
        FakeRow(27561, "C"),
    ]

    ctx = FakeContext(rows)

    # using distinct registered on context (no explicit fields)
    q = select(distinct(ctx)).where(ClientModel.razao == 27560).execute()
    # no explicit distinct fields and no selected fields -> no filtering
    assert len(q) == 3

    # using distinct with explicit field (nome)
    ctx2 = FakeContext(rows)
    q2 = select(distinct(ctx2, ClientModel.nome)).where(ClientModel.razao == 27560).execute()
    # expect unique names among razao==27560 -> names A and B => 2
    assert len(q2) == 2
    names = set(row.nome for row in q2)
    assert names == {"A", "B"}