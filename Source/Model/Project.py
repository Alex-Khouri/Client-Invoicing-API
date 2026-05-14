from ..Globals import *

from ..Model.Invoice.Invoice import Invoice

class Project:
	__name: str
	__invoices: list[Invoice]
	__parentClient: any

	def __init__(self, name:str):
		self.__name = name
		self.__invoices = []
		self.__parentClient = None
	
	def getName(self):
		return self.__name
	
	def getParentClient(self):
		return self.__parentClient
	
	def getInvoice(self):
		return self.__invoices
	
	def setName(self, newName:str):
		if newName == "":
			ERROR(SOURCE.PROJECT, \
		 		"Unable to assign empty name value")
			return False
		
		self.__name = newName
		return True
	
	def setParentClient(self, newClient):
		self.__parentClient = newClient

	def setInvoices(self, newInvoices:list[Invoice]):
		self.__invoices = newInvoices

	def addInvoice(self, newInvoice:Invoice):
		if newInvoice in self.__invoices:
			WARNING(SOURCE.PROJECT, \
		   		f"Unable to add invoice to {self.__name} project, as invoice is already contained within client's collection")
			return False
		
		self.__invoices.append(newInvoice)
		return True

	def removeInvoice(self, invoice:Invoice):
		if invoice not in self.__invoices:
			WARNING(SOURCE.PROJECT, \
		   		f"Unable to remove invoice from {self.__name} project, as invoice isn't contained within current collection")
			return False
		
		self.__invoices.remove(invoice)
		return True
	
	def __str__(self):
		return f"{self.__name}"