class SessionController:
	Users: list
	Sessions: dict	# Key: User, Value: integer

	def __init__(self):
		self.Users = []
		self.Sessions = {}
	
	def __init__(self, users):
		self.Users = list(users)
		self.Sessions = {}
	
	def login(self, username:str, password:str):
		pass
	
	def logout (self, username:str):
		pass