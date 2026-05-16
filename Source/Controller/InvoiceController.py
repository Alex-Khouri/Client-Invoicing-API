from ..Globals import *

from ..Model.Invoice.Invoice import Invoice
from ..Model.Invoice.InvoiceAdjustment import InvoiceAdjustment
from ..Model.Invoice.InvoiceEntry import InvoiceEntry
from ..Model.Project import Project
from ..Model.User import User

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
	
	def updateNextInvoiceID(self, releasedID:int=NULL_INVOICE_ID):
		if releasedID != NULL_INVOICE_ID:
			self.__nextInvoiceID = min(self.__nextInvoiceID, releasedID)
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
		newID = self.__nextInvoiceID
		newInvoice = Invoice(SOURCE.INVOICE_CONTROLLER, newID, project)
		self.__invoices[newID] = newInvoice
		self.updateNextInvoiceID()
		self.__invoiceAdjustments[newInvoice] = []
		project.addInvoice(newInvoice)
		return newInvoice

	def deleteInvoice(self, invoiceID:int):
		invoice = self.getInvoice(invoiceID)
		releasedID = invoiceID
		success = self.__invoices.pop(releasedID, None) is not None and \
					self.__invoiceAdjustments.pop(invoice, None) is not None
		self.updateNextInvoiceID(releasedID)
		parentProject = invoice.getParentProject()
		if parentProject is not None:
			parentProject.removeInvoice(invoice)
		return success

	def adjustInvoice(self, user:User, invoice:Invoice,
						action:INVOICE_ACTION, amount:float, description:str):
		if action == INVOICE_ACTION.ADJUST:
			# Don't assign 'parentInvoice' references for Invoice Entry and Invoice Adjustment,
			# as these are assigned within the Invoice class when the adjustment is applied
			# (including the subsequent addition of the invoice entry).
			entry = InvoiceEntry(amount, description)
			adjustment = InvoiceAdjustment(entry, INVOICE_ENTRY.ADD, user)
			success = invoice.applyAdjustment(adjustment)
			if success:
				adjustments = self.__invoiceAdjustments.setdefault(invoice, [])
				adjustments.append(adjustment)
			return success
		elif action == INVOICE_ACTION.DRAFT:
			invoice.draft()
			return True
		elif action == INVOICE_ACTION.APPROVE:
			invoice.approve()
			return True
		elif action == INVOICE_ACTION.SEND:
			invoice.send()
			return True
		elif action == INVOICE_ACTION.PAY:
			invoice.pay()
			return True
		else:
			return False	# Don't raise warning, as this may be due to user error