import json

from ORM_IXC.interfaces import IModel

def makeJson(fileName: str, models: IModel | list[IModel]) -> None:
    if isinstance(models, list):
        modelsList = []
        for model in models:
            modelsList.append(model.to_dict())
    else:
        modelsList = models.to_dict()

    with open(fileName + '.json', 'w') as file:
         file.write(json.dumps(modelsList, indent=4))
    print(f"arquivo {fileName}.json criado com sucesso")
