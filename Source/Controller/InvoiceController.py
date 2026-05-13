from ..Globals import *

from ..Model.Invoice.Invoice import Invoice
from ..Model.Invoice.InvoiceAdjustment import InvoiceAdjustment
from ..Model.Client import Client
from ..Model.Project import Project

class InvoiceController:
	__clients: dict[str:Client]
	__projects: dict[str:Project]
	__invoices: dict[int:Invoice]
	__invoiceAdjustments: dict[Invoice:list[InvoiceAdjustment]]
	__nextInvoiceID: int
	
	def __init__(self):
		self.__clients = {}
		self.__projects = {}
		self.__invoices = {}
		self.__invoiceAdjustments = {}
		self.__nextInvoiceID = MIN_INVOICE_ID
	
	def cycleNextInvoiceID(self):
		while self.__nextInvoiceID in self.__invoices.keys:
			self.__nextInvoiceID += 1
			if self.__nextInvoiceID > MAX_INVOICE_ID:
				self.__nextInvoiceID = MIN_INVOICE_ID
	
	def getInvoice(self, invoiceID:int):
		return self.__invoices.get(invoiceID, None)

	def createInvoice(self, project:Project):
		newInvoice = Invoice(project)
		newID = self.__nextInvoiceID
		self.__invoices[newID] = newInvoice
		self.cycleNextInvoiceID()
		self.__invoiceAdjustments[newInvoice] = []
		return newInvoice

	def deleteInvoice(self, invoice:Invoice):
		releasedID = invoice.getID()
		success = self.__invoices.pop(releasedID, None) is not None
		success = success and self.__invoiceAdjustments.pop(releasedID, None) is not None
		self.__nextInvoiceID = min(self.__nextInvoiceID, releasedID)
		parentProject = invoice.getParentProject()
		if parentProject is not None:
			parentProject.removeInvoice(invoice)
		return success

	def adjustInvoice(self, invoice:Invoice):
		# TODO!: Finish this
		pass

	def draftInvoice(self, invoice:Invoice):
		# TODO!: Finish this
		pass

	def approveInvoice(self, invoice:Invoice):
		# TODO!: Finish this
		pass
	
	def sendInvoice(self, invoice:Invoice):
		# TODO!: Finish this
		pass
	
	def payInvoice(self, invoice:Invoice):
		# TODO!: Finish this
		pass