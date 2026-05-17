from ..Globals import *

from .InvoiceController import InvoiceController

from ..Model.Client import Client
from ..Model.Invoice import Invoice
from ..Model.Project import Project
from ..Model.User import User

class ClientProjectController:
	__clients: dict[str, Client]	# Client Name -> Client
	__projects: dict[str, dict[str, Project]]	# Client Name -> Project Name -> Project
	__invoiceControllers: dict[Project, InvoiceController]

	def __init__(self):
		self.__clients = {}
		self.__projects = {}
		self.__invoiceControllers = {}
	
	def getClient(self, name:str):
		return self.__clients.get(name, None)

	def getAllClients(self):
		return list(self.__clients.values())
	
	def getProject(self, clientName:str, projectName:str):
		self.__projects.get(clientName, []).get(projectName, None)
	
	def getInvoiceController(self, project:Project):
		return self.__invoiceControllers.get(project, None)
	
	def setClients(self, clients:list[Client]):
		self.__clients.clear()
		self.__projects.clear()
		self.__invoiceControllers.clear()
		for client in clients:
			clientName = client.GetName()
			self.__clients[clientName] = client
			self.__projects[clientName] = {}
			for project in client.getProjects():
				self.__projects[clientName][project.getName()] = project
				self.__invoiceControllers[project] = InvoiceController(project)
	
	def addClient(self, newClient:Client):
		self.__clients[newClient.getName()] = newClient
		self.__projects[newClient.getName()] = {}
		for project in newClient.getProjects():
			self.__projects[newClient.getName()][project.getName()] = project

	def createClient(self, clientName:str):
		newClient = Client(clientName)
		self.addClient(newClient)
		return newClient
	
	def addProject(self, client:Client, newProject:Project):
		clientName = client.getName()
		if clientName not in self.__clients.keys() or \
			client not in self.__clients.values():
			WARNING(SOURCE.CLIENT_PROJECT_CONTROLLER,
		   		f"{newProject.getName()} added without parent client ({clientName}) already added. Projects' clients should be added before their respective projects.")
			self.__clients[clientName] = client
		clientProjects = self.__projects.setdefault(clientName, [])
		clientProjects[newProject.getName()] = newProject
		# Only create new invoice controller for this project if one doesn't exist
		self.__invoiceControllers.setdefault(newProject, InvoiceController(newProject))
		client.addProject(newProject)
		return newProject

	def createProject(self, clientName:str, projectName:str):
		client = self.getClient(clientName)
		if client == None:
			return None
		newProject = Project(projectName, client)
		self.addProject(client, newProject)
		return newProject
	
	def removeClient(self, client:Client):
		clientName = client.getname()
		success = self.__clients.pop(clientName, None) != None
		success = success and self.__projects.pop(clientName, None) != None
		for project in client.getProjects():
			success = success and self.__invoiceControllers.pop(project, None) != None
		client.clearProjects()
		return success
	
	def removeProject(self, client:Client, project:Project):
		# Success = false if client or project names don't exist at respective collection layers
		success = self.__projects.setdefault(client.getName(),
									   			[]).pop(project.getName(), None) != None
		for project in client.getProjects():
			success = success and self.__invoiceControllers.pop(project, None) != None
		success = success and client.removeProject(project)
		return success
	
	def createInvoice(self, project:Project):
		invoiceController = self.getInvoiceController(project)
		if invoiceController == None:
			return None
		return invoiceController.createInvoice()
	
	def deleteInvoice(self, project:Project, invoiceID:int):
		invoiceController = self.getInvoiceController(project)
		if invoiceController == None:
			return False
		return invoiceController.deleteInvoice(invoiceID)
	
	def adjustInvoice(self, project:Project, user:User, invoice:Invoice,
						action:INVOICE_ACTION, amount:float, description:str):
		invoiceController = self.getInvoiceController(project)
		if invoiceController == None:
			return False
		return invoiceController.adjustInvoice(user, invoice, action, amount, description)