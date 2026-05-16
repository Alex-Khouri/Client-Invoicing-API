from ...Globals import *

from .InvoiceEntry import InvoiceEntry
from ..User import User

class InvoiceAdjustment:
	__entry: InvoiceEntry
	__type: INVOICE_ENTRY
	__user: User
	__parentInvoice: any

	def __init__(self, entry:InvoiceEntry=None,
			  		type:INVOICE_ENTRY=INVOICE_ENTRY.NULL, user:User=None):
		self.__entry = entry
		self.__type = type
		self.__user = user
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
	
	def setType(self, newType:INVOICE_ENTRY):
		self.__type = newType
	
	def setUser(self, newUser):
		self.__user = newUser
	
	def setParentInvoice(self, newInvoice):
		self.__parentInvoice = newInvoice
	
	def isValid(self):
		return self.__user is not None and \
			(self.__type == INVOICE_ENTRY.ADD and self.__entry is not None or \
				self.__type == INVOICE_ENTRY.REMOVE and self.__entry is not None)