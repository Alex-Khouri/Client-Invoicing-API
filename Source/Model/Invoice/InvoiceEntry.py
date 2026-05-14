from ...Globals import *

from datetime import date

class InvoiceEntry:
	__name: str
	__amount: float
	__date: date
	__parentInvoice: any

	def __init__(self, name:str, amount:float):
		self.__name = name
		self.__amount = amount
		self.__date = date.today()
		self.__parentInvoice = None
	
	def getName(self):
		return self.__name
	
	def getAmount(self):
		return self.__amount
	
	def getDate(self):
		return self.__date
	
	def getParentInvoice(self):
		return self.__parentInvoice
	
	def setName(self, newName:str):
		if newName == "":
			ERROR(SOURCE.INVOICE_ENTRY, "Unable to assign empty name value")
			return False

		self.__name = newName
		return True
	
	def setAmount(self, newAmount:float):
		self.__amount = newAmount

	def setParentInvoice(self, newInvoice):
		self.__parentInvoice = newInvoice