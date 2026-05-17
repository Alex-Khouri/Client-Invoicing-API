from ..Globals import *

from ..Model.User import User

class UserAccessController:
	__users: dict[str, User]	# Username -> User
	__sessionTokens: dict[int, User]	# Session Token -> User
	__nextSessionToken: int
	
	def __init__(self, users:list[User]=[]):
		self.__users = {}
		for user in users:
			self.__users[user.getUsername()] = user
		self.__sessionTokens = {}
		self.__nextSessionToken = MIN_SESSION_TOKEN
	
	def cycleSessionToken(self):
		while self.__nextSessionToken in self.__sessionTokens.keys():
			self.__nextSessionToken += 1
			if self.__nextSessionToken > MAX_SESSION_TOKEN:
				self.__nextSessionToken = MIN_SESSION_TOKEN

	def getUser(self, username:str):
		return self.__users.get(username, None)

	def getUserFromToken(self, token:int):
		return self.__sessionTokens.get(token, None)
	
	def getAllUserSessionTokens(self, targetToken:int):
		tokens = []
		targetUser = self.__sessionTokens.get(targetToken, None)
		if targetUser is None:
			return tokens
		
		for key, value in self.__sessionTokens.items():
			if value is targetUser:
				tokens.append(key)
		
		return tokens

	def register(self, username:str, password:str, role:USER_ROLE):
		if username in self.__users.keys() or \
			len(username) < 1 or len(password) < 1 or role == USER_ROLE.NULL:
			return False
		
		self.__users[username] = User(username, password, role)
		return True

	def login(self, username:str, password:str):
		user = self.getUser(username)
		if user is None:
			return NULL_SESSION_TOKEN
		
		if (password != user.getPassword()):
			return NULL_SESSION_TOKEN

		newSessionToken = self.__nextSessionToken
		self.__sessionTokens[newSessionToken] = user
		self.cycleSessionToken() # This must be done after new token is stored in collection
		return newSessionToken
	
	def logoutSession(self, sessionToken:int):
		success = self.__sessionTokens.pop(sessionToken, None) is not None
		if success:
			self.__nextSessionToken = min(self.__nextSessionToken, sessionToken)
		return success

	def logoutAllSessions(self, sessionToken:int):
		success = True
		sessionTokens = list(self.getAllUserSessionTokens(sessionToken))
		WARNING_IF(len(sessionTokens) < 0,
			SOURCE.USER_ACCESS_CONTROLLER,
			f"Logout for all sessions triggered for user with no active session tokens")
		for token in sessionTokens:
			success = success and self.logoutSession(token)
		return success
	
	def userCanPerformInvoiceAction(self, sessionToken:int, action:INVOICE_ACTION):
		user = self.__sessionTokens.get(sessionToken, None)
		if user == None:
			ERROR(SOURCE.USER_ACCESS_CONTROLLER,
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
			WARNING(SOURCE.USER_ACCESS_CONTROLLER,
		   		f"Invalid invoice action checked for user permission: {action}")
			return False