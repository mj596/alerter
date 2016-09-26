import sqlite3

class localDBConnector():
    createTable = """
                    CREATE TABLE alerter (
                    UUID VARCHAR2(100) PRIMARY KEY,
                    LEVEL VARCHAR2(10),
                    TIMESTAMP VARCHAR2(100),
                    BODY VARCHAR2(512));
                    """


    def __init__(self):
        self.connection = None
        self.cursor = None
        self.dbfilename = "alerter.db"

    def connect(self):
        self.connection = sqlite3.connect(self.dbfilename)
        print('Connected to', self.dbfilename)
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.connection.close()
        print('Disconnected')

    def execute(self, query, verbose=False):
        self.cursor.execute(query)
        result = []
        for row in self.cursor:
            result.append(row)
        if verbose:
            print('Query:', str(len(result)), 'rows')
        return result

    def commit(self):
        self.connection.commit()

    def insert(self, message):
        QInsertLine = "insert into AQData select "
        for i in range(len(message)):
            QInsertLine += "\'" + str(message[i]) + "\'"
            if i != len(message)-1:
                QInsertLine += ","
        QInsertLine += ' where not exists (select MSG_ID from AQData where MSG_ID = '
        QInsertLine += "\'" + str(message[0]) + "\')"
        QInsertLine += ";"
        print(QInsertLine)
        self.execute(QInsertLine)
