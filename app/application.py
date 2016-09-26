from flask import Flask

class Application(Flask):

    def __init__(self):
        Flask.__init__(self, __name__)

        self.config['SECRET_KEY'] = 'secret!'
        self.config['DEBUG'] = False

        self.messages = []        
        self.data = None

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data
