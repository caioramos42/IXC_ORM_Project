// ============================================================
//  GERADOR DE DATACLASS PYTHON — versão refatorada
//  ✅ Ordena obrigatórios antes dos opcionais
//  ✅ Gera dtoConvert corretamente
//  ✅ Gera helpers automáticos
//  ✅ Gera enums corretamente
//  ✅ Usa kw_only=True
//  ✅ Mantém defaults corretos
//  ✅ Evita TypeError do dataclass
//  ✅ Gera arquivo Python limpo
// ============================================================

// IIFE — isola o escopo para evitar "already been declared" ao rodar
// múltiplas vezes no mesmo contexto (console, bookmarklet, etc.)
;(function () {

// ── 1. LEITURA DO DOM ──────────────────────────────────────

const campoElements = document.getElementsByClassName(
  "spectrum-Heading spectrum-Heading--P click_campos"
);
const infoElements = document.querySelectorAll(
  ".spectrum-Body.spectrum-Body--P > ul"
);

// ── 2. NOME DA CLASSE ──────────────────────────────────────

const rawClassName = document.getElementsByClassName(
  "spectrum-BigSubtleLink"
)[0].innerText.split(" ");

const classNameFinal = rawClassName
  .map((w) => w.charAt(0).toUpperCase() + w.slice(1))
  .join("");

// ── 3. PAYLOAD (defaults vindos do HTML) ──────────────────

const html = document.getElementById("c-python").innerHTML;
const match = html.match(/payload\s*=\s*json\.dumps\(([\s\S]*?)\)/);
const payloadLines = match
  ? match[1].replace("{", "").replace("}", "").split(",\n")
  : [];

const payloadDefaults = new Map();
for (const p of payloadLines) {
  const parts = p.trim().split(": ");
  if (parts.length >= 2) {
    const k = parts[0].replaceAll("'", "").trim();
    const v = parts.slice(1).join(": ").replaceAll("'", "").trim();
    payloadDefaults.set(k, v);
  }
}

// ── 4. MODELAGEM (campos × metadados) ─────────────────────

/**
 * @typedef {{ meta: Map<string,string>, enumLines: string[]|null, type: string, required: boolean, defaultValue: string|null }} FieldInfo
 */

/** @type {Map<string, FieldInfo>} */
const modelagem = new Map();

for (let i = 0; i < campoElements.length; i++) {
  const nomeCampo = campoElements[i].innerText.trim();
  const meta = new Map();

  const liItems = infoElements[i].querySelectorAll("li");
  for (const li of liItems) {
    const [key, ...rest] = li.innerHTML.split(":");
    meta.set(key.trim(), rest.join(":").trim());
  }

  modelagem.set(nomeCampo, meta);
}

// ── 5. ANALISA CADA CAMPO ─────────────────────────────────

/** @type {Array<{ name: string, info: FieldInfo }>} */
const fields = [];

/** @type {string[]} */
const enumBlocks = [];

for (const [name, meta] of modelagem) {
  /** @type {FieldInfo} */
  const info = {
    meta,
    enumLines: null,
    type: "str",
    required: meta.get("Campo obrigatório") !== "Não",
    defaultValue: null,
  };

  if (name === "id") {
    info.type = "int";
    info.required = true;
    fields.push({ name: "id_autoincrement", info });
    continue;
  }

  const valoresDisp = meta.get("Valores disponíveis");
  const tipoCampo = meta.get("Tipo de campo") ?? "";

  // ── ENUM ──
  if (valoresDisp !== undefined) {
    const enumClassName =
      name.charAt(0).toUpperCase() + name.slice(1) + "Enum";
    const rawValues = valoresDisp.split("<br>").slice(1, -1);
    const enumEntries = [];

    for (const val of rawValues) {
      const [code, ...labelParts] = val.split("=");
      const codeClean = code
        .trim()
        .normalize("NFD")
        .replace(/[\u0300-\u036f]/g, "");
      const enumKey = labelParts
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

      enumEntries.push({ enumKey, codeClean });

      // verifica se o payload default bate com este valor
      const payloadVal = payloadDefaults.get(name);
      if (payloadVal !== undefined && payloadVal === codeClean) {
        info.defaultValue = `${enumClassName}.${enumKey}`;
      }
    }

    // monta bloco enum
    let block = `class ${enumClassName}(Enum):\n`;
    for (const { enumKey, codeClean } of enumEntries) {
      block += `    ${enumKey} = '${codeClean}'\n`;
    }
    enumBlocks.push(block);

    info.type = enumClassName;
    info.enumLines = enumEntries.map((e) => e.enumKey);
  }

  // ── TEXTO ──
  else if (
    tipoCampo === "Campo de texto" ||
    tipoCampo === "" ||
    tipoCampo === "Campo de área de texto" ||
    tipoCampo === "Caixa de seleção"
  ) {
    info.type = "str";
    if (!info.required) info.defaultValue = "''";
  }

  // ── INT (busca avançada) ──
  else if (tipoCampo === "Campo de busca avançada") {
    info.type = "int";
    if (!info.required) info.defaultValue = "None";
  }

  // ── FALLBACK ──
  else {
    info.type = "Any";
    if (!info.required) info.defaultValue = "None";
  }

  // campos opcionais sem default explícito recebem None
  if (!info.required && info.defaultValue === null) {
    info.defaultValue = "None";
  }

  fields.push({ name, info });
}

// ── 6. ORDENA: obrigatórios primeiro, depois opcionais ────

const required = fields.filter(
  ({ info }) => info.required && info.defaultValue === null
);
const optional = fields.filter(
  ({ info }) => !info.required || info.defaultValue !== null
);
const sortedFields = [...required, ...optional];

// ── 7. DETECTA IMPORTS NECESSÁRIOS ────────────────────────

const needsAny = fields.some(({ info }) => info.type === "Any");
const needsOptional = fields.some(
  ({ info }) => !info.required || info.defaultValue === "None"
);

// ── 8. GERAÇÃO DO CÓDIGO PYTHON ───────────────────────────

const lines = [];

// --- imports ---
lines.push("from __future__ import annotations");
lines.push("from dataclasses import dataclass, field");
{
  const typingImports = [];
  if (needsAny) typingImports.push("Any");
  if (needsOptional) typingImports.push("Optional");
  if (typingImports.length) {
    lines.push(`from typing import ${typingImports.join(", ")}`);
  }
}
lines.push("from enum import Enum");
lines.push("");

// --- enums ---
if (enumBlocks.length) {
  lines.push(
    "#" + "-".repeat(32) + " ENUMERADORES " + "-".repeat(32) + "#"
  );
  for (const block of enumBlocks) {
    lines.push(block);
  }
}

// --- dataclass ---
lines.push("@dataclass(kw_only=True)");
lines.push(`class ${classNameFinal}:`);

for (const { name, info } of sortedFields) {
  const fieldName = name === "id" ? "id_autoincrement" : name;
  let typePart = info.type;

  if (!info.required || info.defaultValue === "None") {
    typePart = `Optional[${typePart}]`;
  }

  let line = `    ${fieldName}: ${typePart}`;

  if (info.defaultValue !== null) {
    line += ` = ${info.defaultValue}`;
  }

  lines.push(line);
}

// --- to_dict ---
lines.push("");
lines.push("    def to_dict(self) -> dict:");
lines.push("        return {");
for (const { name, info } of sortedFields) {
  const fieldName = name === "id" ? "id_autoincrement" : name;
  let expr;

  if (fieldName === "id_autoincrement") {
    expr = `str(self.${fieldName})`;
  } else if (info.enumLines !== null) {
    expr = `self.${fieldName}.value if self.${fieldName} is not None else ''`;
  } else if (info.type === "int") {
    expr = `str(self.${fieldName}) if self.${fieldName} is not None else ''`;
  } else {
    expr = `self.${fieldName} if self.${fieldName} is not None else ''`;
  }

  lines.push(`            '${fieldName}': ${expr},`);
}
lines.push("        }");

// --- helpers ---
lines.push("");
lines.push("    def is_valid(self) -> bool:");
const requiredNames = required.map(({ name }) =>
  name === "id" ? "id_autoincrement" : name
);
if (requiredNames.length) {
  const checks = requiredNames
    .map((n) => `self.${n} is not None`)
    .join(" and ");
  lines.push(`        return ${checks}`);
} else {
  lines.push("        return True");
}

lines.push("");
lines.push("    def __repr__(self) -> str:");
// Monta o f-string corretamente: {self.campo!r} sem chaves duplicadas
const reprParts = requiredNames.map((n) => `${n}={self.${n}!r}`).join(", ");
lines.push(`        return f"${classNameFinal}(${reprParts})"`);

// --- dtoConvert ---
lines.push("");
lines.push(
  "#" + "-".repeat(30) + " CONVERSOR DTO " + "-".repeat(30) + "#"
);
lines.push(`def dto_convert(data: dict) -> ${classNameFinal}:`);
lines.push(`    return ${classNameFinal}(`);

for (const { name, info } of sortedFields) {
  const fieldName = name === "id" ? "id_autoincrement" : name;
  let expr;

  if (fieldName === "id_autoincrement") {
    expr = `int(data.get('id_autoincrement', 0))`;

  } else if (info.enumLines !== null) {
    const enumCls = info.type;
    if (info.required) {
      // obrigatório: lança KeyError se ausente (sem None), tipo bate com o dataclass
      expr = `${enumCls}(data['${fieldName}'])`;
    } else {
      // opcional: aceita None, tipo é Optional[EnumX]
      expr = `${enumCls}(data['${fieldName}']) if data.get('${fieldName}') else None`;
    }

  } else if (info.type === "int") {
    if (info.required) {
      expr = `int(data['${fieldName}'])`;
    } else {
      expr = `int(data['${fieldName}']) if data.get('${fieldName}') else None`;
    }

  } else {
    // str e Any — required usa get com '' como fallback seguro
    expr = `data.get('${fieldName}', '')`;
  }

  lines.push(`        ${fieldName}=${expr},`);
}
lines.push("    )");

// --- resultado final ---
const resultado = lines.join("\n") + "\n";
console.log(resultado);

// ── 9. DOWNLOAD ───────────────────────────────────────────

const blob = new Blob([resultado], { type: "text/plain" });
const link = document.createElement("a");
link.href = URL.createObjectURL(blob);
link.download = classNameFinal + ".py";
document.body.appendChild(link);
link.click();
document.body.removeChild(link);
URL.revokeObjectURL(link.href);

})(); // fim da IIFE
