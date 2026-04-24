let campos = document.getElementsByClassName("spectrum-Heading spectrum-Heading--P click_campos");
let infos = document.querySelectorAll(".spectrum-Body.spectrum-Body--P > ul");

const modelagem = new Map();

//pegando dict json
const html = document.getElementById('c-python').innerHTML;

const match = html.match(/payload\s*=\s*json\.dumps\(([\s\S]*?)\)/);

const payload = match ? match[1].replace("{", "").replace("}","").split(",\n") : null;


let MyclassName = document.getElementsByClassName("spectrum-BigSubtleLink")[0].innerText.split(" ");
let classNameFinal = "";
for (c of MyclassName){
    classNameFinal += c.charAt(0).toUpperCase() + c.slice(1)
}

let newDict = new Map();

for(p of payload){
    let dictFormat = p.trim().split(": ");
    newDict.set(dictFormat[0].replaceAll("\'",""), dictFormat[1].replaceAll("\'",""))
}

//dasdaasddasdas
for (let i = 0; i < campos.length; i++) {
    let modAux = new Map();

    let allInfo = infos[i].querySelectorAll("li");

    for (let info of allInfo) {
        let [key, ...rest] = info.innerHTML.split(":");
        let value = rest.join(":").trim();
        modAux.set(key.trim(), value);
        //console.log(key + ": "+  rest);
    }

    let nomeCampo = campos[i].innerText.trim();
    modelagem.set(nomeCampo, modAux);
}

// Gerando código Python
let file = "from dataclasses import dataclass\n";
let constructorHeader = "@dataclass\nclass "+ classNameFinal +":\n\t";
let constructorBody = "";
let posinit = ""
let toDict = "\tdef to_dict(self):\n \t\treturn{\n"


let enums = "\n#--------------------------------ENUMERADORES-----------------------------------#\nfrom enums import Enum\n";
let i = 0;
for (let [key, value] of modelagem) {
    let defaultValue = undefined;
    if (key === "id"){
        constructorHeader += "id_autoincrement: int";
        toDict += "\t\tself.id = str(self.id)\n"
    }else{
        constructorHeader += key;
        if (value.get("Valores disponíveis") !== undefined){
            enums += "class "+ key.charAt(0).toUpperCase() + key.slice(1) + "Enum(Enum)" + ":\n";
            let valoresDisponiveis = value.get("Valores disponíveis").split("<br>").slice(1, -1);
            for(val of valoresDisponiveis){
                let keyv = val.split("=");
                enums += "\t" + keyv[1].toUpperCase().trim().normalize('NFD')
                .replace(/[\u0300-\u036f]/g, "")
                .replaceAll(" ", "_")
                .toUpperCase()
                .replace(/\(.*\)/g, "")
                .replaceAll("/","_")
                .replaceAll("-","_") + " = \'" + keyv[0].trim().normalize('NFD').replace(/[\u0300-\u036f]/g, "") + "\'\n";
                
                if (newDict.get(key) !== undefined){ 
                    if(newDict.get(key) === keyv[0].trim().normalize('NFD').replace(/[\u0300-\u036f]/g, "")){
                        defaultValue = key.charAt(0).toUpperCase() + key.slice(1) + "Enum" + ".";
                        // Para pegar o nome da constante que acabamos de criar acima:
                        defaultValue += keyv[1].toUpperCase().trim().normalize('NFD')
                        .replace(/[\u0300-\u036f]/g, "")
                        .replaceAll(" ", "_")
                        .toUpperCase()
                        .replaceAll("-","_")
                        .replaceAll("/","_")
                        .replace(/\(.*\)/g, "");
                    }
                }
            }
            enums += "\n";
            constructorHeader +=": " + key.charAt(0).toUpperCase() + key.slice(1) + "Enum";
            if (defaultValue !== undefined){
                if(value.get("Campo obrigatório") === "Não" || value.get("Campo obrigatório") === ""){
                    constructorHeader +=" | None";
                }
                constructorHeader += " = " + defaultValue;
            } 
            if (value.get("Campo obrigatório") === "Não"){
                posinit = " self." + key + ".value if self." + key + " is not None else \'\'";
                toDict += "\t\t\t\'" + key + "\': " + posinit + ",\n";
            }
        }
        else if (value.get("Tipo de campo") === "Campo de texto" || value.get("Tipo de campo") === "" || value.get("Tipo de campo") === "Campo de área de texto" || value.get("Tipo de campo") === 'Caixa de seleção') {
            if(newDict.get(campos[i]) !== ''){
                constructorHeader +=": str";
                if (value.get("Campo obrigatório") === "Não" || value.get("Campo obrigatório") === ""){
                    if(newDict.get(key) === ''){
                        constructorHeader +=" = \'\'";
                    }else{
                        constructorHeader +=" = \'" + newDict.get(key) + "\'";
                    }
                }
            } 
        }
        if (value.get("Tipo de campo") === "Campo de busca avançada"){
            constructorHeader +=": int";
            if (value.get("Campo obrigatório") === "Não"){
                posinit = " str(self." + key + ") if self." + key + " is not None else \'\'";
                toDict += "\t\t\t\'" + key + "\': " + posinit + ",\n";
            }
        }
        if ((value.get("Campo obrigatório") === "Não" || value.get("Campo obrigatório") === "") && !((value.get("Tipo de campo") === "Campo de texto" || value.get("Tipo de campo") === "" || value.get("Tipo de campo") === "Campo de área de texto" || value.get("Tipo de campo") === 'Caixa de seleção')) && value.get("Valores disponíveis") === undefined){
            constructorHeader +=" | None";
        }
    }
    constructorHeader += "\n\t";
    i++;
}

constructorHeader = constructorHeader.replace(/, $/, "");
constructorHeader += "\n";
toDict += "\t\t}" 

let resultado = file + constructorHeader + constructorBody + toDict + enums ;
console.log(resultado);
// ---- GERAR ARQUIVO PYTHON PARA DOWNLOAD ----
const blob = new Blob([resultado], { type: "text/plain" });
const link = document.createElement("a");

link.href = URL.createObjectURL(blob);
link.download = classNameFinal + ".py";

document.body.appendChild(link);
link.click();
document.body.removeChild(link);

URL.revokeObjectURL(link.href);