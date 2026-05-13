from ..Globals import *

from ..Model.User import User

class SessionController:
	__users: list[User]
	__sessionCodes: dict[int:User]
	__nextSessionCode: int

	def __init__(self):
		self.__users = []
		self.__sessionCodes = {}
		self.__nextSessionCode = MIN_SESSION_CODE
	
	def __init__(self, users:list[User]):
		self.__users = list(users)
		self.__sessionCodes = {}
		self.__nextSessionCode = MIN_SESSION_CODE
	
	def cycleSessionCode(self):
		while self.__nextSessionCode in self.__sessionCodes.keys:
			self.__nextSessionCode += 1
			if self.__nextSessionCode > MAX_SESSION_CODE:
				self.__nextSessionCode = MIN_SESSION_CODE

	def getUser(self, username:str):
		for user in self.__users:
			if user.getUsername() == username:
				return user
		return None
	
	def getActiveUserSessionCodes(self, targetCode:int):
		codes = []
		targetUser = self.__sessionCodes.get(targetCode, None)
		if targetUser is None:
			return codes
		
		for key, value in self.__sessionCodes:
			if value == targetUser:
				codes.append(key)
		
		return codes

	def login(self, username:str, password:str):
		user = self.getUser(username)
		if user is None:
			return NULL_SESSION_CODE
		
		if (password != user.getPassword()):
			return NULL_SESSION_CODE

		newSessionCode = self.__nextSessionCode
		self.__sessionCodes[newSessionCode] = user
		self.cycleSessionCode()
		return newSessionCode
	
	def logoutSession(self, sessionCode:int):
		success = self.__sessionCodes.pop(sessionCode, None) is not None
		if success:
			self.__nextSessionCode = min(self.__nextSessionCode, sessionCode)
		return success

	def logoutAllSessions(self, sessionCode:int):
		success = True
		for code in self.getActiveUserSessionCodes(sessionCode):
			success = success and self.logoutSession(code)
		return success