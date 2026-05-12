from .. import *

class User:
	username: str
	password: str
	role: USER_ROLE

	def __init__(self, username, password, role=USER_ROLE.NULL):
		self.username = username
		self.password = password
		self.role = role
	
	def getUsername(self):
		return self.username
	
	def getPassword(self):
		return self.password
	
	def getRole(self):
		return self.role

	def setUsername(self, newUsername:str):
		if newUsername == "":
			ERROR(SOURCE.USER,\
		 		"Unable to assign empty username value")
			return False

		self.username = newUsername
		return True
	
	def setPassword(self, newPassword:str):
		if newPassword == "":
			ERROR(SOURCE.USER, "Unable to assign empty password value")
			return False

		self.password = newPassword
		return True
	
	def setRole(self, newRole:USER_ROLE):
		if newRole == USER_ROLE.NULL:
			ERROR(SOURCE.USER, "Unable to assign null role value")
			return False
		
		self.role = newRole
		return True