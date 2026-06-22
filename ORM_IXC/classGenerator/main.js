;(function () {
//https://wikiapiprovedor.ixcsoft.com.br/formulario.php?form=radusuarios
// ────────────────────────────────────────────────────────────
// LEITURA DOM
// ────────────────────────────────────────────────────────────

const campoElements = document.getElementsByClassName(
  "spectrum-Heading spectrum-Heading--P click_campos"
);

const infoElements = document.querySelectorAll(
  ".spectrum-Body.spectrum-Body--P > ul"
);

// ────────────────────────────────────────────────────────────
// NOME CLASSE
// ────────────────────────────────────────────────────────────

const rawClassName = document.getElementsByClassName(
  "spectrum-BigSubtleLink"
)[0].innerText.split(" ");

const classNameFinal = rawClassName
  .map((w) => w.charAt(0).toUpperCase() + w.slice(1))
  .join("");

const modelName = `${classNameFinal}Model`;

// ────────────────────────────────────────────────────────────
// PAYLOAD DEFAULTS
// ────────────────────────────────────────────────────────────

const html = document.getElementById("c-python").innerHTML;

const match = html.match(
  /payload\s*=\s*json\.dumps\(([\s\S]*?)\)/
);

const tableMatch = html.match(
  /webservice\/v1\/([^"']+)/
);

const tableName = tableMatch
  ? tableMatch[1]
  : classNameFinal.toLowerCase();

const payloadLines = match
  ? match[1]
      .replace("{", "")
      .replace("}", "")
      .split(",\n")
  : [];

const payloadDefaults = new Map();

for (const p of payloadLines) {

  const parts = p.trim().split(": ");

  if (parts.length >= 2) {

    const k = parts[0]
      .replaceAll("'", "")
      .trim();

    const v = parts
      .slice(1)
      .join(": ")
      .replaceAll("'", "")
      .trim();

    payloadDefaults.set(k, v);
  }
}

// ────────────────────────────────────────────────────────────
// MODELAGEM
// ────────────────────────────────────────────────────────────

const modelagem = new Map();

for (let i = 0; i < campoElements.length; i++) {

  const nomeCampo = campoElements[i]
    .innerText
    .trim();

  const meta = new Map();

  const liItems =
    infoElements[i].querySelectorAll("li");

  for (const li of liItems) {

    const [key, ...rest] =
      li.innerHTML.split(":");

    meta.set(
      key.trim(),
      rest.join(":").trim()
    );
  }

  modelagem.set(nomeCampo, meta);
}

// ────────────────────────────────────────────────────────────
// ANALISE CAMPOS
// ────────────────────────────────────────────────────────────

const fields = [];
const enumBlocks = [];

for (const [name, meta] of modelagem) {

  const info = {
    meta,
    enumLines: null,
    type: "str",
    required:
      meta.get("Campo obrigatório") !== "Não",
    defaultValue: null,
  };

  if (name === "id") {

    info.type = "int";
    info.required = false;

    fields.push({ name, info });

    continue;
  }

  const valoresDisp =
    meta.get("Valores disponíveis");

  const tipoCampo =
    meta.get("Tipo de campo") ?? "";

  // ───────────────── ENUM ─────────────────

  if (valoresDisp !== undefined) {

    const enumClassName =
      name.charAt(0).toUpperCase() +
      name.slice(1) +
      "Enum";

    const rawValues =
      valoresDisp
        .split("<br>")
        .slice(1, -1);

    const enumEntries = [];

    for (const val of rawValues) {

      const [code, ...labelParts] =
        val.split("=");

      const codeClean =
        code
          .trim()
          .normalize("NFD")
          .replace(/[\u0300-\u036f]/g, "");

      const enumKey =
        labelParts
          .join("=")
          .toUpperCase()
          .trim()
          .normalize("NFD")
          .replace(/[\u0300-\u036f]/g, "")
          .replaceAll(" ", "_")
          .replace(/\(.*?\)/g, "")
          .replaceAll("/", "_")
          .replaceAll("-", "_")
          .trim();

      enumEntries.push({
        enumKey,
        codeClean
      });

      const payloadVal =
        payloadDefaults.get(name);

      if (
        payloadVal !== undefined &&
        payloadVal === codeClean
      ) {
        info.defaultValue =
          `${enumClassName}.${enumKey}`;
      }
    }

    let block =
      `class ${enumClassName}(Enum):\n`;

    for (const e of enumEntries) {
      block +=
        `    ${e.enumKey} = '${e.codeClean}'\n`;
    }

    enumBlocks.push(block);

    info.type = enumClassName;
    info.enumLines = enumEntries;
  }

  // ───────────────── TEXTO ─────────────────

  else if (
    tipoCampo === "Campo de texto" ||
    tipoCampo === "" ||
    tipoCampo === "Campo de área de texto" ||
    tipoCampo === "Caixa de seleção"
  ) {

    info.type = "str";

    if (!info.required) {
      info.defaultValue = "''";
    }
  }

  // ───────────────── BUSCA AVANCADA ─────────────────

  else if (
    tipoCampo === "Campo de busca avançada"
  ) {

    info.type = "int";

    if (!info.required) {
      info.defaultValue = "None";
    }
  }

  else {

    info.type = "str";

    if (!info.required) {
      info.defaultValue = "None";
    }
  }

  if (
    !info.required &&
    info.defaultValue === null
  ) {
    info.defaultValue = "None";
  }

  fields.push({ name, info });
}

// ────────────────────────────────────────────────────────────
// ORDENA
// ────────────────────────────────────────────────────────────

const required = fields.filter(
  ({ info }) =>
    info.required &&
    info.defaultValue === null
);

const optional = fields.filter(
  ({ info }) =>
    !info.required ||
    info.defaultValue !== null
);

const sortedFields = [
  ...required,
  ...optional
];

// ────────────────────────────────────────────────────────────
// GERAÇÃO ARQUIVO ENUM SEPARADO
// ────────────────────────────────────────────────────────────

const enumModuleName =
  classNameFinal.charAt(0).toLowerCase() +
  classNameFinal.slice(1);

const enumFileLines = [];

enumFileLines.push("from enum import Enum");
enumFileLines.push("");
enumFileLines.push("");

if (enumBlocks.length) {
  for (const block of enumBlocks) {
    enumFileLines.push(block);
  }
}

const enumResult =
  enumFileLines.join("\n") + "\n";

// ────────────────────────────────────────────────────────────
// GERAÇÃO PYTHON MODEL
// ────────────────────────────────────────────────────────────

const lines = [];

// imports

lines.push(
  "from __future__ import annotations"
);

lines.push(
  "from typing import Optional"
);

lines.push(
  "from ORM_IXC.interfaces import IModelWithId"
);

if (enumBlocks.length) {

  lines.push(
    `from ORM_IXC.enums.${enumModuleName} import *`
  );
}

lines.push(
  "from ORM_IXC.statemants.maps.mapper import Mapped, field as mapped_field"
);

lines.push(
  "from ORM_IXC.statemants.maps.metaManager import MetaModels"
);

lines.push(
  "from ORM_IXC.models.tableModels.defaultModel import BaseModel"
);

lines.push("");
lines.push("");

// class

lines.push("@MetaModels");

lines.push(
  `class ${modelName}(IModelWithId, BaseModel):`
);

// fields

for (const { name, info } of sortedFields) {

  let mappedType;

  if (
    !info.required ||
    info.defaultValue === "None"
  ) {

    mappedType =
      `Mapped[Optional[${info.type}]]`;

  } else {

    mappedType =
      `Mapped[${info.type}]`;
  }

  let line =
    `    ${name} :${mappedType}`;

  if (info.defaultValue !== null) {

    line +=
      ` = mapped_field(${info.defaultValue})`;
  }

  lines.push(line);
}

// table

lines.push("");
lines.push("    @property");
lines.push("    def table(self) -> str:");
lines.push(
  `        return "${tableName}"`
);

// serialize enum

lines.push("");
lines.push(
  "    def _serialize_enum_and_str(self, value) -> str:"
);

lines.push(
  '        """Serializa um valor de enum ou retorna string vazia se None"""'
);

lines.push(
  "        if value is None:"
);

lines.push(
  "            return ''"
);

lines.push(
  "        if hasattr(value, 'value'):"
);

lines.push(
  "            return str(value.value)"
);

lines.push(
  "        return str(value)"
);

// to_dict

lines.push("");
lines.push(
  "    def to_dict(self) -> dict:"
);

lines.push(
  "        def serialize(value) -> str:"
);

lines.push(
  "            if value is None:"
);

lines.push(
  "                return ''"
);

lines.push(
  "            raw = getattr(value, 'value', value)"
);

lines.push(
  "            return '' if raw is None else str(raw)"
);

lines.push("");
lines.push("        data = {");

for (const { name, info } of sortedFields) {

  let value;

  if (info.type === "int") {

    value =
      `str(self.${name}) if self.${name} is not None else ''`;

  } else {

    value =
      `self._serialize_enum_and_str(self.${name}) if self.${name} is not None else ''`;
  }

  lines.push(
    `            '${name}': ${value},`
  );
}

lines.push("        }");

lines.push(
  "        return {key: serialize(value) for key, value in data.items()}"
);

// is_valid

lines.push("");
lines.push(
  "    def is_valid(self) -> bool:"
);

const requiredChecks =
  required.map(
    ({ name }) =>
      `self.${name} is not None`
  );

lines.push(
  `        return ${requiredChecks.join(" and ")}`
);

// ────────────────────────────────────────────────────────────
// GERA CONTEXT
// ────────────────────────────────────────────────────────────

const contextLines = [];

contextLines.push(
  "from typing import Any, List, Iterator, cast"
);

contextLines.push(
  "from ORM_IXC.interfaces.IContext import IContext"
);

contextLines.push(
  "from ORM_IXC.context.defaultActions.defaultActions import DefaultActions"
);

contextLines.push(
  "from ORM_IXC.context.request.manager import Manager"
);

contextLines.push(
  `from ORM_IXC.models.tableModels.${enumModuleName}Model import ${modelName}`
);

contextLines.push(
  "from ORM_IXC.models.searchUtils.searchModel import SearchModule"
);

contextLines.push(
  "import requests"
);

contextLines.push("");
contextLines.push("");

contextLines.push(
  `class ${classNameFinal}(IContext[${modelName}, ${modelName}], DefaultActions):`
);

contextLines.push(
  "    def __init__(self, manager: Manager):"
);

contextLines.push(
  `        DefaultActions.__init__(self, ${modelName}, manager)`
);

contextLines.push("");

contextLines.push(
  `    def Add(self, obj: ${modelName}) -> Any:`
);

contextLines.push(
  "        return self._MakePost(obj)"
);

contextLines.push("");

contextLines.push(
  `    def Update(self, obj: ${modelName}, search: SearchModule) -> list[requests.Response]:`
);

contextLines.push(
  "        return self._MakeUpdate(obj, search)"
);

contextLines.push("");

contextLines.push(
  "    def Delete(self, search: SearchModule) -> List[requests.Response]:"
);

contextLines.push(
  "        return super()._MakeDelete(search)"
);

contextLines.push("");

contextLines.push(
  "    def DeleteById(self, id: int) -> Any:"
);

contextLines.push(
  `        raise NotImplementedError("DeleteById não implementado para ${classNameFinal}")`
);

contextLines.push("");

contextLines.push(
  `    def SelectAll(self) -> List[${modelName}]:`
);

contextLines.push(
  `        return cast(List[${modelName}], self._SearchAll())`
);

contextLines.push("");

contextLines.push(
  "    def SelectByFilter(self, search: Any) -> List[" +
    modelName +
    "]:"
);

contextLines.push(
  `        return cast(List[${modelName}], self.getByFilter(search))`
);

contextLines.push("");

contextLines.push(
  "    def SelectByFilterAssync("
);

contextLines.push(
  "        self,"
);

contextLines.push(
  "        search: SearchModule,"
);

contextLines.push(
  "        page_size: int = 172"
);

contextLines.push(
  `    ) -> Iterator[${modelName}]:`
);

contextLines.push(
  `        return cast(Iterator[${modelName}], super().cursorByFilter(search, page_size))`
);

contextLines.push("");

contextLines.push(
  `    def SelectAllAssync(self) -> Iterator[${modelName}]:`
);

contextLines.push(
  `        return cast(Iterator[${modelName}], super()._SelectAllAssync())`
);

const contextResult =
  contextLines.join("\n") + "\n";

const resultado =
  lines.join("\n") + "\n";

console.log("=== MODEL ===");
console.log(resultado);
console.log("=== ENUM ===");
console.log(enumResult);
console.log("=== CONTEXT ===");
console.log(contextResult);

// ────────────────────────────────────────────────────────────
// DOWNLOAD HELPER
// ────────────────────────────────────────────────────────────

function download(content, filename) {
  const blob = new Blob(
    [content],
    { type: "text/plain" }
  );
  const link = document.createElement("a");
  link.href = URL.createObjectURL(blob);
  link.download = filename;
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
  URL.revokeObjectURL(link.href);
}

// ────────────────────────────────────────────────────────────
// DOWNLOADS
// ────────────────────────────────────────────────────────────

// 1. Model
download(resultado, `${modelName}.py`);

// 2. Enum (arquivo separado)
if (enumBlocks.length) {
  download(enumResult, `${enumModuleName}.py`);
}

// 3. Context
download(contextResult, `${classNameFinal}.py`);

})();