from ... import *

class Invoice:
	# TODO!: Use 'parent' variable prefix for 2-way link references (for clarity)
	__entries: list[InvoiceEntry]
	__total: float
	__state: INVOICE_STATE
	__project: Project

	def __init__(self, amount, state=INVOICE_STATE.DRAFT):
		self.__entries = []
		self.__total = amount
		self.__state = state
		self.__project = None
	
	def getEntries(self):
		return self.__entries

	def getTotal(self):
		return self.__total
	
	def getState(self):
		return self.__state
	
	def getProject(self):
		return self.__project
	
	def setEntries(self, newEntries:list[InvoiceEntry]):
		self.__entries = list(newEntries)
		self.__total = 0
		for entry in self.__entries:
			self.__total += entry.getAmount()

	def setState(self, newState:INVOICE_STATE):
		if newState == INVOICE_STATE.NULL:
			return	# Null should only be used as default starting value
		
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
			WARNING(SOURCE.INVOICE,\
		   		f"Invalid attempted state transition:\n----Current State: {self.__state}\n----New State: {newState}")
			return False
		
	def setProject(self, newProject:Project):
		self.__project = newProject
	
	def addEntry(self, newEntry:InvoiceEntry):
		if newEntry in self.__entries:
			ERROR(SOURCE.INVOICE,\
		 		f"Unable to add {newEntry.getName()} entry to {self} invoice")
			return False
		
		self.__entries.append(newEntry)
		self.__total += newEntry.getAmount()
		return True
	
	def removeEntry(self, entry:InvoiceEntry):
		if entry in self.__entries:
			ERROR(SOURCE.INVOICE,\
		 		f"Unable to remove {entry.getName()} entry from {self} invoice")
			return False
		
		self.__entries.remove(entry)
		self.__total -= entry.getAmount()
		return True

	def __str__(self):
		return f"{self.__project.getName() if self.__project is not None else "NONE"}"