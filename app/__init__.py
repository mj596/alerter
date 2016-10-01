from app.application import Application
from flask_socketio import SocketIO, emit
import uuid
# from app.LocalData import LocalData
from app.DbData import DbData

app = Application()
# data = LocalData()
data = DbData()
app.set_data(data)
socketio = SocketIO(app)

from app import views
