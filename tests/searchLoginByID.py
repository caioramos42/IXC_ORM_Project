from ORM_IXC.context import Login
from ORM_IXC.context.request import Manager
import os
from dotenv import load_dotenv
from ORM_IXC.utils.makejson import makeJson
load_dotenv()

host = str(os.getenv("IXC_HOST"))
token = str(os.getenv("IXC_TOKEN"))

manager = Manager(host, token)
login = Login(manager)

makeJson('testFile', login.SelectAll())

