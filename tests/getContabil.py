from ORM_IXC.context.contabil import Contabil
from ORM_IXC.context.request.manager import Manager
import sys
import os
from dotenv import load_dotenv

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
load_dotenv()

def getOs():
    manager = Manager(os.getenv("IXC_HOST"), os.getenv("IXC_TOKEN"))

    service_order = Contabil(manager)
    #print(service_order.SearchById(305290).json())
    with open("Contabil.json", "w") as f:
        f.write(service_order.SearchById('id_contabil').text)
getOs()