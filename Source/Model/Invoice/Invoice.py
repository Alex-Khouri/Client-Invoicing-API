from ... import *

class Invoice:
	__entries: list[InvoiceEntry]
	__total: float
	__state: INVOICE_STATE
	__parentProject: Project

	def __init__(self, amount, state=INVOICE_STATE.DRAFT):
		self.__entries = []
		self.__total = amount
		self.__state = state
		self.__parentProject = None
	
	def getEntries(self):
		return self.__entries

	def getTotal(self):
		return self.__total
	
	def getState(self):
		return self.__state
	
	def getParentProject(self):
		return self.__parentProject
	
	def setEntries(self, newEntries:list[InvoiceEntry]):
		if self.__state == INVOICE_STATE.PAID:
			WARNING(SOURCE.INVOICE, \
		   		f"Attempting to reassign entries on paid invoice")
			return

		self.__entries = list(newEntries)
		self.__total = 0
		for entry in self.__entries:
			self.__total += entry.getAmount()
		
		self.setState(INVOICE_STATE.DRAFT)

	def setState(self, newState:INVOICE_STATE):
		if newState == INVOICE_STATE.NULL:
			return False	# Null should only be used as default starting value
		
		# Invoice state change workflow
		if (self.__state == INVOICE_STATE.NULL or \
			self.__state == INVOICE_STATE.APPROVED or \
			self.__state == INVOICE_STATE.SENT) and newState == INVOICE_STATE.DRAFT or \
		self.__state == INVOICE_STATE.DRAFT and newState == INVOICE_STATE.APPROVED or \
		self.__state == INVOICE_STATE.APPROVED and newState == INVOICE_STATE.SENT or \
		self.__state == INVOICE_STATE.SENT and newState == INVOICE_STATE.PAID:
			self.__state = newState
			return True
		else:
			WARNING(SOURCE.INVOICE, \
		   		f"Invalid attempted state transition:\n----Current State: {self.__state}\n----New State: {newState}")
			return False
		
	def setParentProject(self, newProject:Project):
		self.__parentProject = newProject
	
	def addEntry(self, newEntry:InvoiceEntry):
		if self.__state == INVOICE_STATE.PAID:
			WARNING(SOURCE.INVOICE, \
		   		f"Entries cannot be added to paid invoices")
			return False
		
		if newEntry is None:
			ERROR(SOURCE.INVOICE, \
				f"Unable to add {newEntry.getName()} entry to {self} invoice, due to empty object reference")
			return False
		
		if newEntry in self.__entries:
			ERROR(SOURCE.INVOICE, \
		 		f"Unable to add {newEntry.getName()} entry to {self} invoice, as invoice already contains entry")
			return False
		
		self.__entries.append(newEntry)
		self.__total += newEntry.getAmount()
		newEntry.setParentInvoice(self)
		self.setState(INVOICE_STATE.DRAFT)
		return True
	
	def removeEntry(self, entry:InvoiceEntry):
		if self.__state == INVOICE_STATE.PAID:
			WARNING(SOURCE.INVOICE, \
		   		f"Attempting to remove entry from paid invoice")
			return False

		if entry is None:
			ERROR(SOURCE.INVOICE, \
				f"Unable to remove {entry.getName()} entry from {self} invoice, due to empty object reference")
			return False

		if entry not in self.__entries:
			ERROR(SOURCE.INVOICE, \
		 		f"Unable to remove {entry.getName()} entry from {self} invoice, as invoice doesn't contain entry")
			return False
		
		self.__entries.remove(entry)
		self.__total -= entry.getAmount()
		entry.setParentInvoice(None)
		self.setState(INVOICE_STATE.DRAFT)
		return True
	
	def applyAdjustment(self, adjustment:InvoiceAdjustment):
		if not adjustment.isValid():
			ERROR(SOURCE.INVOICE, \
		 		f"Unable to apply invalid adjustment to {self} invoice")
			return False

		if adjustment.getType() == INVOICE_ADJUSTMENT.ADD:
			success = self.addEntry(adjustment.getEntry())
			if success:
				adjustment.setParentInvoice(self)
			return success
		elif adjustment.getType() == INVOICE_ADJUSTMENT.REMOVE:
			success = self.removeEntry(adjustment.getEntry())
			if success:
				adjustment.setParentInvoice(self)
			return success
		else:
			ERROR(SOURCE.INVOICE, \
		 		f"Unable to process adjustment due to invalid type: {adjustment.getType()}")
			return False

	def __str__(self):
		clientName = self.__parentProject.getParentClient().getName() if \
						self.__parentProject is not None and \
						self.__parentProject.getParentClient() is not None else \
							"NONE"
		projectName = self.__parentProject.getName() if \
						self.__parentProject is not None else \
							"NONE"
		return f"{clientName}/{projectName}"