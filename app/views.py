from flask import render_template
from app import app, socketio
from flask import request, jsonify
from flask_socketio import emit, send
import uuid
import datetime

def get_now():
    return str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", title='Home', timestamp=get_now() )

@app.route('/add', methods=['POST'])
def add_post():
    message_in = request.json

    if message_in['timestamp'] is None:
         timestamp = get_now()
    else:
        timestamp = message_in['timestamp']
    
    message_out = {
        'level': message_in['level'],
        'timestamp': timestamp,
        'body': message_in['body']
}
    app.get_data().add( message_in['level'], timestamp, message_in['body']  )
    return jsonify(message_out)

@app.route('/add', methods=['GET'])
def add_get():

    if request.args.get('timestamp') is None:
        timestamp = get_now()
    else:
        timestamp = request.args.get('timestamp')

    message_out = {
        'uuid': str(uuid.uuid1())[:8],
        'level': request.args.get('level'),
        'timestamp': timestamp,
        'body': request.args.get('body')
    }
    app.get_data().add( request.args.get('level'), timestamp, request.args.get('body') )
    socketio.emit('message')
    return jsonify({'success':True}), 200, {'ContentType':'application/json'}
    #return render_template("add.html", data=message_out, title='Add')

@socketio.on('message')
def handle_message():
    print('--> received message <--')
    socketio.emit('message')

@app.route('/getData', methods=['GET'])
def getData_get():
    return jsonify(app.get_data().get_all())

@app.route('/showData', methods=['GET'])
def showData_get():
    return render_template("showData.html",
                           title='Data')

@socketio.on('delete')
def delete_message(message):
    app.get_data().remove(message['uuid'])

	
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    form = LoginForm()
    if form.validate_on_submit():
        # Login and validate the user.
        # user should be an instance of your `User` class
        login_user(user)

        flask.flash('Logged in successfully.')

        next = flask.request.args.get('next')
        # next_is_valid should check if the user has valid
        # permission to access the `next` url
        if not next_is_valid(next):
            return flask.abort(400)

        return flask.redirect(next or flask.url_for('index'))
    return flask.render_template('login.html', form=form)