from .. import *

class Project:
	__name: str
	__client: Client
	__invoices: list[Invoice]

	def __init__(self, name:str):
		self.__name = name
		self.__client = None
		self.__invoices = []
	
	def getName(self):
		return self.__name
	
	def getClient(self):
		return self.__client
	
	def getInvoice(self):
		return self.__invoices
	
	def setName(self, newName:str):
		if newName == "":
			ERROR(SOURCE.PROJECT,\
		 		"Unable to assign empty name value")
			return
		
		self.__name = newName
	
	def setClient(self, newClient:Client):
		self.__client = newClient

	def setInvoices(self, newInvoices:list[Invoice]):
		self.__invoices = newInvoices

	def addInvoice(self, newInvoice:Invoice):
		if newInvoice in self.__invoices:
			WARNING(SOURCE.PROJECT,\
		   		f"Unable to add invoice to {self.__name} project, as invoice is already contained within client's collection")
			return False
		
		self.__invoices.append(newInvoice)
		return True

	def removeInvoice(self, invoice:Invoice):
		if invoice not in self.__invoices:
			WARNING(SOURCE.PROJECT,\
		   		f"Unable to remove invoice from {self.__name} project, as invoice isn't contained within current collection")
			return False
		
		self.__invoices.remove(invoice)
		return True
	
	def __str__(self):
		return f"{self.__name}"