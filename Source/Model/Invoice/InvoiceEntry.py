from ... import *
from datetime import date

class InvoiceEntry:
	__name: str
	__amount: float
	__date: datetime.date
	__invoice: Invoice

	def __init__(self, name:str, amount:float):
		self.__name = name
		self.__amount = amount
		self.__date = date.today()
		self.__invoice = None
	
	def getName(self):
		return self.__name
	
	def getAmount(self):
		return self.__amount
	
	def getDate(self):
		return self.__date
	
	def getInvoice(self):
		return self.__invoice
	
	def setName(self, newName:str):
		if newName == "":
			ERROR(SOURCE.INVOICE_ENTRY, "Unable to assign empty name value")
			return False

		self.__name = newName
		return True
	
	def setAmount(self, newAmount:float):
		self.__amount = newAmount

	def setInvoice(self, newInvoice:Invoice):
		self.__invoice = newInvoice