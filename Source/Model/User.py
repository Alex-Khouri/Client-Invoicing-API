from .. import *

class User:
	__username: str
	__password: str
	__role: USER_ROLE

	def __init__(self, username, password, role=USER_ROLE.NULL):
		self.__username = username
		self.__password = password
		self.__role = role
	
	def getUsername(self):
		return self.__username
	
	def getPassword(self):
		return self.__password
	
	def getRole(self):
		return self.__role

	def setUsername(self, newUsername:str):
		if newUsername == "":
			ERROR(SOURCE.USER, \
		 		"Unable to assign empty username value")
			return False

		self.__username = newUsername
		return True
	
	def setPassword(self, newPassword:str):
		if newPassword == "":
			ERROR(SOURCE.USER, "Unable to assign empty password value")
			return False

		self.__password = newPassword
		return True
	
	def setRole(self, newRole:USER_ROLE):
		if newRole == USER_ROLE.NULL:
			ERROR(SOURCE.USER, "Unable to assign null role value")
			return False
		
		self.__role = newRole
		return True