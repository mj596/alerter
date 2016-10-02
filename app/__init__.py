from app.application import Application
from flask_socketio import SocketIO, emit
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user 
import uuid

from app.LocalData import LocalData
from app.DbData import DbData

app = Application()
#data = LocalData()
data = DbData()
app.set_data(data)
socketio = SocketIO(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

from app import views
