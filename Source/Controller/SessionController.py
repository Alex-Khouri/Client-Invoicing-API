from .. import *

class SessionController:
	__users: list[User]
	__sessions: dict[str:User]

	def __init__(self):
		self.__users = []
		self.__sessions = {}
	
	def __init__(self, users:list[User]):
		self.__users = list(users)
		self.__sessions = {}
	
	def login(self, username:str, password:str):
		pass
	
	def logout (self, username:str):
		pass