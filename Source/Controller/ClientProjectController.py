from .InvoiceController import InvoiceController

from ..Model.Client import Client
from ..Model.Project import Project

class ClientProjectController:
	__clients: list[Client]
	__projects: list[Project]
	__invoiceControllers: dict[Project, InvoiceController]

	def __init__(self):
		self.__clients = []
		self.__projects = []
		self.__invoiceControllers = {}