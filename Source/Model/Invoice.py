from .. import *

class Invoice:
	amount: float
	state: INVOICE_STATE
	project: Project

	def __init__(self, amount, project, state=INVOICE_STATE.DRAFT):
		self.amount = amount
		self.state = state
		self.project = project
	
	def getAmount(self):
		return self.amount
	
	def getState(self):
		return self.state
	
	def getProject(self):
		return self.project
	
	def setAmount(self, newAmount:float):
		self.amount = newAmount

	def setState(self, newState:INVOICE_STATE):
		if newState == INVOICE_STATE.NULL:
			return	# Null should only be used as default starting value
		
		# Invoice state change workflow
		if (self.state == INVOICE_STATE.NULL or \
	  			self.state == INVOICE_STATE.APPROVED or \
				self.state == INVOICE_STATE.SENT) and newState == INVOICE_STATE.DRAFT or \
			self.state == INVOICE_STATE.DRAFT and newState == INVOICE_STATE.APPROVED or \
			self.state == INVOICE_STATE.APPROVED and newState == INVOICE_STATE.SENT or \
			self.state == INVOICE_STATE.SENT and newState == INVOICE_STATE.PAID:
			self.state = newState
			return True
		else:
			WARNING(SOURCE.INVOICE,)
			return False
		
	def setProject(self, newProject):
		self.project = newProject