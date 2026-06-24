from datetime import datetime, timedelta

from ORM_IXC.models.tableModels.serviceOrderModel import ServiceOrderModel
from ORM_IXC.context.contextModels.serviceOrder import ServiceOrder
from ORM_IXC.models.tableModels.assuntoModel import AssuntoModel
from ORM_IXC.context.contextModels.assunto import Assunto
from ORM_IXC.context.request import Manager
from ORM_IXC.statemants.CRUD.select import select
from ORM_IXC.utils.pythonFormats import to_pandas_dataframe
from dotenv import load_dotenv

import os

from ORM_IXC.utils.makejson import makeJson

load_dotenv()

host = str(os.getenv("IXC_HOST"))
token = str(os.getenv("IXC_TOKEN"))

manager = Manager(host, token)
serviceOrder = ServiceOrder(manager)
assunto = Assunto(manager)


yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
yyesterday = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')

query = select(serviceOrder)\
                        .columns(ServiceOrderModel.data_abertura,
                                 AssuntoModel.assunto)\
                        .where(
                           (ServiceOrderModel.data_abertura >= yyesterday + ' 00:00:00') &
                           (ServiceOrderModel.data_abertura <= yesterday + ' 23:59:59') &
                           ServiceOrderModel.id_assunto.In(1,3,4,5)
                           )\
                            .join(assunto, ServiceOrderModel.id_assunto == AssuntoModel.id)\
                        .limit(3000)\
                        .execute()
                        
#makeJson("myos", query)
pandas = to_pandas_dataframe(query)
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Converter data
pandas['su_oss_chamado.data_abertura'] = pd.to_datetime(
    pandas['su_oss_chamado.data_abertura']
)

# Criar posição Y para cada assunto
assuntos = pandas['su_oss_assunto.assunto'].unique()

y_map = {
    assunto: idx + 1
    for idx, assunto in enumerate(assuntos)
}

plt.figure(figsize=(18, 8))

for assunto_nome in assuntos:

    dados = pandas[
        pandas['su_oss_assunto.assunto'] == assunto_nome
    ]

    plt.bar(
        dados['su_oss_chamado.data_abertura'],
        [y_map[assunto_nome]] * len(dados),
        width=0.2,
        label=assunto_nome
    )

plt.yticks(
    list(y_map.values()),
    list(y_map.keys())
)

plt.gca().xaxis.set_major_formatter(
    mdates.DateFormatter('%d/%m/%Y')
)

plt.xticks(rotation=45)

plt.title("Timeline de Chamados")
plt.xlabel("Data")
plt.ylabel("Assunto")
plt.legend(title="Assunto BD")
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()