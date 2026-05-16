from ..Globals import *

from ..Model.Invoice.Invoice import Invoice

class Project:
	__name: str
	__invoices: dict[int, Invoice]
	__parentClient: any

	def __init__(self, name:str, client:any=None):
		self.__name = name
		self.__invoices = {}
		self.__parentClient = client
	
	def getName(self):
		return self.__name
	
	def getParentClient(self):
		return self.__parentClient
	
	def getInvoices(self):
		return list(self.__invoices.values())

	def getInvoice(self, id:int):
		return self.__invoices.get(id, None)
	
	def setName(self, newName:str):
		if newName == "":
			ERROR(SOURCE.PROJECT,
		 		"Unable to assign empty name value")
			return False
		
		self.__name = newName
		return True
	
	def setParentClient(self, newClient):
		self.__parentClient = newClient

	def setInvoices(self, newInvoices:list[Invoice]):
		self.__invoices.clear()
		for invoice in newInvoices:
			self.__invoices[invoice.getID()] = invoice

	def addInvoice(self, newInvoice:Invoice):
		if newInvoice in self.__invoices.values() or newInvoice.getID() in self.__invoices.keys():
			WARNING(SOURCE.PROJECT,
		   		f"Unable to add invoice to {self.__name} project, as invoice is already contained within client's collection")
			return False
		
		self.__invoices[newInvoice.getID()] = newInvoice
		return True

	def removeInvoice(self, id:int):
		success = self.__invoices.pop(id, None) != None
		WARNING_IF(not success,
			SOURCE.PROJECT,
			f"Unable to remove invoice {id} from {self.__name} project, as collection doesn't contain any invoices with that ID")
		return success
	
	def __str__(self):
		return f"{self.__name}"