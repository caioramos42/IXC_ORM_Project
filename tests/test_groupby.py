from ORM_IXC.statemants.CRUD.select import select
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


def test_groupby_filters_unique_rows_by_field_after_execute():
    rows = [
        FakeRow(27560, "A"),
        FakeRow(27560, "A"),
        FakeRow(27560, "B"),
        FakeRow(27560, "B"),
    ]
    ctx = FakeContext(rows)

    grouped = select(ctx).where(ClientModel.razao == 27560).groupby(ClientModel.nome).execute()

    assert len(grouped) == 2
    assert {row.nome for row in grouped} == {"A", "B"}


def test_groupby_filters_unique_rows_by_field_after_cursor():
    rows = [
        FakeRow(27560, "A"),
        FakeRow(27560, "A"),
        FakeRow(27560, "B"),
        FakeRow(27560, "B"),
    ]
    ctx = FakeContext(rows)

    grouped = list(select(ctx).where(ClientModel.razao == 27560).groupby(ClientModel.nome).cursor())

    assert len(grouped) == 2
    assert {row.nome for row in grouped} == {"A", "B"}
