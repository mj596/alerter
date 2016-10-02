import uuid
import app.LocalDBConnector as LocalDBConnector
import os

class DbData():

    def __init__(self):
        self.dbfilename = "alerter.db"
        self.dbname = "ALERTER"
        self.username = "alerter"
        self.password = "alerter2016"
        self.table = "MESSAGES"   
         
        db_exists = False
        
        if os.path.exists(self.dbfilename):
            db_exists = True
        
        self.db = LocalDBConnector.LocalDBConnector(verbose=False)
        self.db.setCredentials(self.username, self.password, self.dbfilename, self.dbname)
        self.db.connect()
        
        self.createTable = "CREATE TABLE " + self.table + " (uuid TEXT, level TEXT, timestamp TEXT, body TEXT, status NUMBER);"
        
        if db_exists is False:
            self.db.execute(self.createTable)
            self.db.commit()
        
    def add(self, level, timestamp, body):
        id = str(uuid.uuid1()).replace("-","")
        insert = "INSERT INTO " + self.table + " (uuid, level, timestamp, body, status) VALUES (\"" + id + "\",\"" + level + "\",\"" + timestamp + "\",\"" + body + "\",0);"
        print(insert)
        self.db.execute( insert )
        self.db.commit()
        
    def remove(self, uuid):
        delete = "UPDATE " + self.table + " SET STATUS = 1 WHERE uuid = \"" + uuid + "\";"
        self.db.execute( delete )
        self.db.commit()
                
    def get_all(self):
        return self.db.select_all_with_condition(self.table, "timestamp", "status = 0")
        
    def get(self, uuid):
        condition = "status = 0 AND uuid = \"" + uuid + "\""
        return self.db.select_all_with_condition(self.table, "timestamp", condition)
    
if __name__ == "__main__":
    db = DbData()
    db.add("1", "2", "3")
    db.remove("e55e3bd2881011e6b645543357068c14")
    print(db.get_all())
    print(db.get("e3daa1c4881011e69b95543357068c14"))