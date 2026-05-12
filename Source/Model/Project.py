from .. import *

class Project:
	name: str
	client: Client

	def __init__(self, name, client):
		self.name = name
		self.client = client
	
	def getName(self):
		return self.name
	
	def getClient(self):
		return self.client
	
	def setName(self, newName:str):
		if newName == "":
			ERROR(SOURCE.PROJECT,\
		 		"Unable to assign empty name value")
			return
		
		self.name = newName
	
	def setClient(self, newClient:Client):
		self.client = newClient