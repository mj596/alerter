import LocalDBConnector

class AlerterDB:
	createTable = """
		CREATE TABLE MESSAGES (
			UUID TEXT PRIMARY KEY,
			LEVEL TEXT,
            TIMESTAMP TEXT,
			BODY TEXT,
			STATUS NUMBER);
        """
	insertRow = """
		INSERT INTO MESSAGES (UUID, LEVEL, TIMESTAMP, BODY, STATUS) 
		VALUES (1235, "ERROR", "16-25-13 13:43:12", "Jaka wiadomosc", 0);
		"""
		
	selectAll = """SELECT UUID, LEVEL, TIMESTAMP, BODY, STATUS FROM MESSAGES;"""
def main():

	db = LocalDBConnector.LocalDBConnector(verbose=True)
	db.setCredentials("alerter", "alerter2016", "alerter.db", "ALERTER")
	db.connect()
	# db.execute(AlerterDB.createTable)
	#db.execute(AlerterDB.insertRow)
	#db.commit()
	#messages = db.execute(AlerterDB.selectAll)
	#for message in messages:
	#	print(message)
	db.select_all("MESSAGES", "TIMESTAMP")	
    
if __name__ == "__main__":
	main()