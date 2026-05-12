from .. import *

class Adjustment:
	amount: float
	user: User

	def __init__(self, amount, user):
		self.amount = amount
		self.user = user
	
	def getAmount(self):
		return self.amount

	def getUser(self):
		return self.user
	
	def setAmount(self, newAmount):
		self.amount = newAmount
	
	def setUser(self, newUser):
		self.user = newUser