from flask import render_template
from app import app, socketio
from flask import request, jsonify
from flask_socketio import emit, send
import uuid
import datetime
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from flask import Flask, Response, redirect, url_for, request, session, abort

def get_now():
    return str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template("index.html", title='Home', timestamp=get_now())

#@app.route('/add', methods=['POST'])
#def add_post():
#    message_in = request.json
#
#    if message_in['timestamp'] is None:
#         timestamp = get_now()
#    else:
#        timestamp = message_in['timestamp']
#    
#    message_out = {
#        'level': message_in['level'],
#        'timestamp': timestamp,
#        'body': message_in['body']
#}
#    app.get_data().add( message_in['level'], timestamp, message_in['body']  )
#    return jsonify(message_out)

@app.route('/add', methods=['GET'])
def add_get():
    
    if request.args.get('timestamp') is None:
        timestamp = get_now()
    else:
        timestamp = request.args.get('timestamp')
    
    valid_token = "a5D5YS6tEds3H4fgb9ksQDt7128G3ETS"
    
    if request.args.get('token', 0) == valid_token:
        app.get_data().add( request.args.get('level'), timestamp, request.args.get('body') )
        socketio.emit('message')
        return jsonify({'success':True}), 200, {'ContentType':'application/json'}
        #return render_template("add.html", data=message_out, title='Add')
    else:
        return jsonify({'success':False}), 401, {'ContentType':'application/json'}

@socketio.on('message')
def handle_message():
    print('--> received message <--')
    socketio.emit('message')

@app.route('/getData', methods=['GET'])
@login_required
def getData_get():
    return jsonify(app.get_data().get_all())

@app.route('/showData', methods=['GET'])
@login_required
def showData_get():
    return render_template("showData.html",
                           title='Data')

@socketio.on('delete')
def delete_message(message):
    app.get_data().remove(message['uuid'])

	
# silly user model
#class User(UserMixin):
#
#    def __init__(self, id):
#        self.id = id
#        self.name = "user" + str(id)
#        self.password = self.name + "_secret"
#        
#    def __repr__(self):
#        return "%d/%s/%s" % (self.id, self.name, self.password)

class User(UserMixin):

    def __init__(self, id):
        self.id = id
        if self.id == 0:
            self.name = "admin"
            self.password = "alerter2016!"
        if self.id == 1:
            self.name = "viewer"
            self.password = "viewer2016!"
        
    def __repr__(self):
        return "%d/%s/%s" % (self.id, self.name, self.password)

    def get_username(self):
        return self.name
        
    def get_password(self):
        return self.password
        
    def get_id(self):
        return self.id
        
def check_login(username, password, users):
    id = 999
    for user in users:
        if user.get_username() == username and user.get_password() == password:
            id = user.get_id()
            break
        
    return id
        
# create some users with ids 1 to 20       
#users = [User(id) for id in range(1, 21)]

users = [User(0), User(1)]

# somewhere to login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']  
        
        id = check_login( username, password, users)
        if id == 999:
            return abort(401)
        else:
            user = User(id)
            login_user(user)
            session['logged_in'] = True
            return redirect("/")

        #if password == username + "_secret":
        #    id = username.split('user')[1]
        #    user = User(id)
        #    login_user(user)
        #    session['logged_in'] = True
        #    return redirect("/")
        #else:
        #    return abort(401)
    else:
        return render_template("login.html", title="Login")


# somewhere to logout
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")
    #return Response('<p>Logged out</p>')


# handle login failed
@app.errorhandler(401)
def page_not_found(e):
    return redirect("/") 
    #return Response('<p>Login failed</p>')
    
    
# callback to reload the user object        
@app.login_manager.user_loader
def load_user(userid):
    return User(userid)