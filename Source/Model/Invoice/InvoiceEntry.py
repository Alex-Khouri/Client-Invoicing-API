from ...Globals import *

from datetime import date

class InvoiceEntry:
	__date: date
	__amount: float
	__description: str
	__parentInvoice: any

	def __init__(self, name:str, amount:float):
		self.__date = date.today()
		self.__amount = amount
		self.__description = name
		self.__parentInvoice = None
	
	def getDate(self):
		return self.__date
	
	def getAmount(self):
		return self.__amount
	
	def getDescription(self):
		return self.__description
	
	def getParentInvoice(self):
		return self.__parentInvoice
	
	def setAmount(self, newAmount:float):
		self.__amount = newAmount

	def setDescription(self, newName:str):
		if newName == "":
			ERROR(SOURCE.INVOICE_ENTRY, "Unable to assign empty name value")
			return False

		self.__description = newName
		return True

	def setParentInvoice(self, newInvoice):
		self.__parentInvoice = newInvoice

	def __str__(self):
		return f"{self.__date} - {self.__amount} - {self.__description}"