from ... import *

class InvoiceAdjustment:
	__entry: InvoiceEntry
	__type: INVOICE_ADJUSTMENT
	__user: User
	__parentInvoice: Invoice

	def __init__(self):
		self.__entry = None
		self.__type = INVOICE_ADJUSTMENT.NULL
		self.__user = None
		self.__parentInvoice = None
	
	def getEntry(self):
		return self.__entry

	def getType(self):
		return self.__type

	def getUser(self):
		return self.__user
	
	def getParentInvoice(self):
		return self.__parentInvoice
	
	def setEntry(self, newEntry:InvoiceEntry):
		self.__entry = newEntry
	
	def setType(self, newType:INVOICE_ADJUSTMENT):
		self.__type = newType
	
	def setUser(self, newUser):
		self.__user = newUser
	
	def setParentInvoice(self, newInvoice):
		self.__parentInvoice = newInvoice
	
	def isValid(self):
		return self.__user is not None and \
			(self.__type == INVOICE_ADJUSTMENT.ADD and self.__entry is not None or \
				self.__type == INVOICE_ADJUSTMENT.REMOVE and self.__entry is not None)