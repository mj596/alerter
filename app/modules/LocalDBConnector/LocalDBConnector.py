import sqlite3
import os.path

class LocalDBConnector():
    
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.connection = None
        self.cursor = None
        self.dbfilename = None
        self.dbname = None
        self.username = None
        self.password = None

    def connect(self):
        self.connection = sqlite3.connect(self.dbfilename, check_same_thread = False)
        if self.verbose == True:
            print('Connected to', self.dbfilename)
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.connection.close()
        if self.verbose == True:
            print('Disconnected')

    def execute(self, query):
        if self.verbose:
            print('Execute query: ', query)
        self.cursor.execute(query)
        result = []
        for row in self.cursor:
            result.append(row)
        if self.verbose:
            print('Query got: ', str(len(result)), ' rows')
        return result

    def commit(self):
        self.connection.commit()
        
    def setCredentials(self, username, password, dbfilename, dbname):
        self.username = username
        self.password = password
        self.dbfilename = dbfilename
        self.dbname = dbname    
        
    def select_all(self, table, order=None):
        column_names_temp = self.execute("PRAGMA table_info(\"" + table + "\");")
        column_names = []
        select_query = "SELECT "
        for ii in range(len(column_names_temp)):
            column_names.append((column_names_temp[ii])[1])
            select_query += (column_names_temp[ii])[1]
            if ii != len(column_names_temp)-1:
                select_query += ", "
                
        select_query += " FROM " + table
        if order is not None:
            select_query += " ORDER BY date(" + order + ") DESC"
           
        select_query += ";"
        result_array = self.execute( select_query )
        results = []
        for res in result_array:
            result = {}
            for ii in range(len(column_names)):
                result[column_names[ii].lower()] = res[ii]
            
            results.append(result)
           
        return( results )
        
    def select_all_with_condition(self, table, order=None, condition=None):
        column_names_temp = self.execute("PRAGMA table_info(\"" + table + "\");")
        column_names = []
        select_query = "SELECT "
        for ii in range(len(column_names_temp)):
            column_names.append((column_names_temp[ii])[1])
            select_query += (column_names_temp[ii])[1]
            if ii != len(column_names_temp)-1:
                select_query += ", "
                
        select_query += " FROM " + table
        if condition is not None:
            select_query += " WHERE " + condition
        
        if order is not None:
            select_query += " ORDER BY date(" + order + ") DESC"
           
        select_query += ";"

        result_array = self.execute( select_query )
        results = []
        for res in result_array:
            result = {}
            for ii in range(len(column_names)):
                result[column_names[ii].lower()] = res[ii]
            
            results.append(result)
        
        return( results )