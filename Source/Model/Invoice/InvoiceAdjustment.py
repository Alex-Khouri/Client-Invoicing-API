from ... import *

class InvoiceAdjustment:
	__entry: InvoiceEntry
	__user: User
	__invoice: Invoice

	def __init__(self, user:User):
		self.__entry = None
		self.__user = user
		self.__invoice = None
	
	def getEntry(self):
		return self.__entry

	def getUser(self):
		return self.__user
	
	def getInvoice(self):
		return self.__invoice
	
	def setEntry(self, newEntry:InvoiceEntry):
		self.__entry = newEntry
	
	def setUser(self, newUser):
		self.__user = newUser
	
	def setInvoice(self, newInvoice):
		self.__invoice = newInvoice