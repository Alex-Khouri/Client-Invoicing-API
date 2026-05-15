from ..Globals import *

from ..Model.User import User

class SessionController:
	__sessionTokens: dict[int:User]
	__nextSessionToken: int
	
	def __init__(self, users:dict[int:User]={}):
		self.__sessionTokens = users
		self.__nextSessionToken = MIN_SESSION_TOKEN
	
	def cycleSessionToken(self):
		while self.__nextSessionToken in self.__sessionTokens.keys:
			self.__nextSessionToken += 1
			if self.__nextSessionToken > MAX_SESSION_TOKEN:
				self.__nextSessionToken = MIN_SESSION_TOKEN

	def getUser(self, username:str):
		for user in self.__sessionTokens.values:
			if user.getUsername() == username:
				return user
		return None
	
	def targetToken(self, targetToken:int):
		tokens = []
		targetUser = self.__sessionTokens.get(targetToken, None)
		if targetUser is None:
			return tokens
		
		for key, value in self.__sessionTokens:
			if value == targetUser:
				tokens.append(key)
		
		return tokens

	def login(self, username:str, password:str):
		user = self.getUser(username)
		if user is None:
			return NULL_SESSION_TOKEN
		
		if (password != user.getPassword()):
			return NULL_SESSION_TOKEN

		newSessionToken = self.__nextSessionToken
		self.__sessionTokens[newSessionToken] = user
		self.cycleSessionToken()
		return newSessionToken
	
	def logoutSession(self, sessionToken:int):
		success = self.__sessionTokens.pop(sessionToken, None) is not None
		if success:
			self.__nextSessionToken = min(self.__nextSessionToken, sessionToken)
		return success

	def logoutAllSessions(self, sessionToken:int):
		success = True
		for token in self.targetToken(sessionToken):
			success = success and self.logoutSession(token)
		return success
	
	def userCanPerformInvoiceAction(self, sessionToken:int, action:INVOICE_ACTION):
		user = self.__sessionTokens.get(sessionToken, None)
		if user == None:
			ERROR(SOURCE.SESSION_CONTROLLER, \
		 		f"Unable to check user access for {action} invoice action, due to invalid session token: {sessionToken}")
			return False
		
		if action == INVOICE_ACTION.REPORT:
			return user.getRole() == USER_ROLE.MANAGER
		elif action == INVOICE_ACTION.CREATE:
			return user.getRole() == USER_ROLE.STAFF
		elif action == INVOICE_ACTION.DELETE:
			return user.getRole() == USER_ROLE.STAFF
		elif action == INVOICE_ACTION.ADJUST:
			return user.getRole() == USER_ROLE.STAFF
		elif action == INVOICE_ACTION.DRAFT:
			return user.getRole() == USER_ROLE.STAFF
		elif action == INVOICE_ACTION.APPROVE:
			return user.getRole() == USER_ROLE.MANAGER
		elif action == INVOICE_ACTION.SEND:
			return user.getRole() == USER_ROLE.STAFF
		elif action == INVOICE_ACTION.PAY:
			return user.getRole() == USER_ROLE.STAFF
		else:
			WARNING(SOURCE.SESSION_CONTROLLER, \
		   		f"Invalid invoice action checked for user permission: {action}")
			return False