from ..Globals import *

from ..Model.Invoice.Invoice import Invoice
from ..Model.Invoice.InvoiceAdjustment import InvoiceAdjustment
from ..Model.Project import Project

class InvoiceController:
	__invoices: dict[int, Invoice]
	__invoiceAdjustments: dict[Invoice, list[InvoiceAdjustment]]
	__nextInvoiceID: int
	__parentProject: Project
	
	def __init__(self, parentProject:Project=None):
		self.__invoices = {}
		self.__invoiceAdjustments = {}
		self.__nextInvoiceID = MIN_INVOICE_ID
		self.__parentProject = parentProject
	
	def cycleNextInvoiceID(self):
		while self.__nextInvoiceID in self.__invoices.keys():
			self.__nextInvoiceID += 1
			if self.__nextInvoiceID > MAX_INVOICE_ID:
				self.__nextInvoiceID = MIN_INVOICE_ID
	
	def getInvoices(self):
		return list(self.__invoices.values())

	def getInvoice(self, invoiceID:int):
		return self.__invoices.get(invoiceID, None)
	
	def getParentProject(self):
		return self.__parentProject

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