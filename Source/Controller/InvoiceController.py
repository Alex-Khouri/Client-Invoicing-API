from .. import *

class InvoiceController:
	__clients: list[Client]
	__projects: list[Project]
	__invoices: list[Invoice]
	__invoiceAdjustments: list[InvoiceAdjustment]
	
	def __init__(self):
		self.__clients = []
		self.__projects = []
		self.__invoices = []
		self.__invoiceAdjustments = []