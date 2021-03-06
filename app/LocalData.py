import uuid

class LocalData():

	def __init__(self):
		self.messages = [
			{
				'uuid': str(uuid.uuid1())[:8],
				'level': 'ERROR',
				'timestamp': '2016-09-28 12:00:00',
				'body': 'That is an error'
			},
			{
				'uuid': str(uuid.uuid1())[:8], 
				'level': 'WARNING',
				'timestamp': '2016-09-25 12:00:00',
				'body': 'That is just a warning' 
			},
			{
				'uuid': str(uuid.uuid1())[:8],
				'level': 'ERROR',
				'timestamp': '2016-09-28 13:00:00',
				'body': 'That is an error 2'
			},
			{
				'uuid': str(uuid.uuid1())[:8],
				'level': 'INFO',
				'timestamp': '2016-09-28 13:00:00',
				'body': 'That is an information'
			},
			{
				'uuid': str(uuid.uuid1())[:8],
				'level': 'UWAGA',
				'timestamp': '2016-09-11 13:00:00',
				'body': 'Przykładowa informacja'
			}    
		]
		
	def add(self, level, timestamp, body):
		message = {
			'uuid': str(uuid.uuid1())[:8],
			'level': str(level),
			'timestamp': str(timestamp),
			'body': str(body)
		}
		self.messages.append(message)
		
	def remove(self, uuid):
		for index in range(len(self.messages)):
			if uuid == (self.messages[index])['uuid']:
				self.messages.pop(index)
				break
				
	def get_all(self):
		return self.messages
		
	def get(self, uuid):
		for index in range(len(self.messages)):
			if uuid == (self.messages[index])['uuid']:
				return self.messages['index']
	