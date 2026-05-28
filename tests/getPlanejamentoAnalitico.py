from ORM_IXC.context.contextModels.classeFinanceiraAnalitica import PlanejamentoAnalitico
from ORM_IXC.context.request.manager import Manager
import sys
import os
from dotenv import load_dotenv

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
load_dotenv()

def getOs():
    manager = Manager(os.getenv("IXC_HOST"), os.getenv("IXC_TOKEN"))

    service_order = PlanejamentoAnalitico(manager)

    print(service_order.SearchById(0))
getOs()