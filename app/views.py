from flask import render_template
from app import app, socketio
from flask import request, jsonify
from flask_socketio import emit, send
import uuid

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", title='Home')

@app.route('/add', methods=['POST'])
def add_post():
    message_in = request.json
    message_out = {
        'level': message_in['level'],
        'timestamp': message_in['timestamp'],
        'body': message_in['body']
}
    app.get_data().add( message_in['level'], message_in['timestamp'], message_in['body']  )
    return jsonify(message_out)

@app.route('/add', methods=['GET'])
def add_get():
    message_out = {
        'uuid': str(uuid.uuid1())[:8],
        'level': request.args.get('level'),
        'timestamp': request.args.get('timestamp'),
        'body': request.args.get('body')
    }
    app.get_data().add( request.args.get('level'), request.args.get('timestamp'), request.args.get('body') )     
    return render_template("add.html", data=message_out, title='Add')

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
    print('--> Deleting ' + message['uuid'] + ' <--')
    app.get_data().remove(message['uuid'])
    print("--> Did I delete? <--")
