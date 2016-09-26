from app.application import Application
from flask_socketio import SocketIO, emit
import uuid
from app.LocalData import LocalData

app = Application()
data = LocalData()
app.set_data(data)
socketio = SocketIO(app)

from app import views
