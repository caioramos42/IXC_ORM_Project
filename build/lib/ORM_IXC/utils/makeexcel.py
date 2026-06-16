import zipfile
from xml.sax.saxutils import escape


def numero_para_coluna(n):
    resultado = ""
    while n >= 0:
        resultado = chr(n % 26 + 65) + resultado
        n = n // 26 - 1
    return resultado


def makeXlsx(objetos, arquivo_saida="saida"):
    if not objetos:
        raise ValueError("Lista vazia")
    arquivo_saida = f"{arquivo_saida}.xlsx"
    
    # Obtém headers do primeiro objeto usando to_dict()
    headers = list(objetos[0].to_dict().keys())
    linhas = [headers]
    
    # Processa cada objeto usando to_dict()
    for obj in objetos:
        linhas.append(list(obj.to_dict().values()))

    sheet_data = ""

    for row_idx, linha in enumerate(linhas, start=1):
        sheet_data += f'<row r="{row_idx}">'

        for col_idx, valor in enumerate(linha):
            coluna = numero_para_coluna(col_idx)
            celula = f"{coluna}{row_idx}"

            valor = escape(str(valor))

            sheet_data += (
                f'<c r="{celula}" t="inlineStr">'
                f'<is><t>{valor}</t></is>'
                f'</c>'
            )

        sheet_data += "</row>"

    workbook_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"
 xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
 <sheets>
  <sheet name="Planilha1" sheetId="1" r:id="rId1"/>
 </sheets>
</workbook>
"""

    workbook_rels_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
 <Relationship Id="rId1"
  Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet"
  Target="worksheets/sheet1.xml"/>
</Relationships>
"""

    root_rels_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
 <Relationship Id="rId1"
  Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument"
  Target="xl/workbook.xml"/>
</Relationships>
"""

    content_types_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
 <Default Extension="rels"
  ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
 <Default Extension="xml" ContentType="application/xml"/>
 <Override PartName="/xl/workbook.xml"
  ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>
 <Override PartName="/xl/worksheets/sheet1.xml"
  ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
</Types>
"""

    sheet_xml = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">
 <sheetData>
  {sheet_data}
 </sheetData>
</worksheet>
"""
    with zipfile.ZipFile(arquivo_saida, "w", zipfile.ZIP_DEFLATED) as xlsx:
        xlsx.writestr("[Content_Types].xml", content_types_xml)
        xlsx.writestr("_rels/.rels", root_rels_xml)
        xlsx.writestr("xl/workbook.xml", workbook_xml)
        xlsx.writestr("xl/_rels/workbook.xml.rels", workbook_rels_xml)
        xlsx.writestr("xl/worksheets/sheet1.xml", sheet_xml)

    print(f"Arquivo gerado: {arquivo_saida}")
    
    
import zipfile
from xml.sax.saxutils import escape


def _numero_para_coluna(n):
    resultado = ""

    while n >= 0:
        resultado = chr(n % 26 + 65) + resultado
        n = n // 26 - 1

    return resultado


def makeXLSXStream(
    arquivo_saida,
    async_iterador
):
    arquivo_saida = f"{arquivo_saida}.xlsx"
    headers = None
    sheet_data = ""
    row_idx = 1

    for item in async_iterador:
        # Chama to_dict() para obter os dados
        dados = item.to_dict()

        # Cria cabeçalho na primeira iteração
        if headers is None:
            headers = list(dados.keys())
            sheet_data += f'<row r="{row_idx}">'

            for col_idx, header in enumerate(headers):
                coluna = _numero_para_coluna(col_idx)
                celula = f"{coluna}{row_idx}"
                sheet_data += (
                    f'<c r="{celula}" t="inlineStr">'
                    f'<is><t>{escape(str(header))}</t></is>'
                    f'</c>'
                )

            sheet_data += "</row>"
            row_idx += 1

        # Linha de dados
        sheet_data += f'<row r="{row_idx}">'

        for col_idx, header in enumerate(headers):
            coluna = _numero_para_coluna(col_idx)
            celula = f"{coluna}{row_idx}"
            valor = dados.get(header, "")
            sheet_data += (
                f'<c r="{celula}" t="inlineStr">'
                f'<is><t>{escape(str(valor))}</t></is>'
                f'</c>'
            )

        sheet_data += "</row>"
        row_idx += 1

    workbook_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"
 xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
 <sheets>
  <sheet name="Planilha1" sheetId="1" r:id="rId1"/>
 </sheets>
</workbook>
"""

    workbook_rels_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
 <Relationship Id="rId1"
  Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet"
  Target="worksheets/sheet1.xml"/>
</Relationships>
"""

    root_rels_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
 <Relationship Id="rId1"
  Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument"
  Target="xl/workbook.xml"/>
</Relationships>
"""

    content_types_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
 <Default Extension="rels"
  ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
 <Default Extension="xml" ContentType="application/xml"/>
 <Override PartName="/xl/workbook.xml"
  ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>
 <Override PartName="/xl/worksheets/sheet1.xml"
  ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
</Types>
"""

    sheet_xml = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">
 <sheetData>
  {sheet_data}
 </sheetData>
</worksheet>
"""

    with zipfile.ZipFile(
        arquivo_saida,
        "w",
        zipfile.ZIP_DEFLATED
    ) as xlsx:

        xlsx.writestr(
            "[Content_Types].xml",
            content_types_xml
        )

        xlsx.writestr(
            "_rels/.rels",
            root_rels_xml
        )

        xlsx.writestr(
            "xl/workbook.xml",
            workbook_xml
        )

        xlsx.writestr(
            "xl/_rels/workbook.xml.rels",
            workbook_rels_xml
        )

        xlsx.writestr(
            "xl/worksheets/sheet1.xml",
            sheet_xml
        )