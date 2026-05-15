from ..Globals import *

from .InvoiceController import InvoiceController

from ..Model.Client import Client
from ..Model.Project import Project

class ClientProjectController:
	__clients: dict[str, Client]
	__projects: dict[str, Project]
	__invoiceControllers: dict[Project, InvoiceController]

	def __init__(self):
		self.__clients = []
		self.__projects = []
		self.__invoiceControllers = {}
	
	def getClient(self, name:str):
		return self.__clients.get(name, None)

	def getAllClients(self):
		return self.__clients.values
	
	def getProject(self, name:str):
		return self.__projects.get(name, None)

	def getAllProjects(self):
		return self.__projects.values
	
	def getInvoiceController(self, project:Project):
		return self.__invoiceControllers.get(project, None)
	
	def setClients(self, clients:list[Client]):
		self.__clients.clear()
		self.__projects.clear()
		self.__invoiceControllers.clear()
		for client in clients:
			self.__clients[client.getName()] = client
			# Don't use 'setProjects' here because it clears collections on each call
			for project in client.getProjects():
				self.__projects[project.getName()] = project
				self.__invoiceControllers[project] = InvoiceController(project)

	def setProjects(self, projects:list[Project]):
		self.__projects.clear()
		self.__invoiceControllers.clear()
		for project in projects:
			self.__projects[project.getName()] = project
			self.__invoiceControllers[project] = InvoiceController(project)
	
	def addClient(self, client:Client):
		self.__clients[client.getName()] = client
		for project in client.getProjects():
			self.addProject(project)
	
	def addProject(self, project:Project):
		self.__projects[project.getName()] = project
		self.__invoiceControllers[project] = InvoiceController(project)
	
	def removeClient(self, client:Client):
		success = self.__clients.pop(client.getName(), None) != None
		for project in client.getProjects():
			success = success and self.removeProject(project)
		return success
	
	def removeProject(self, project:Project):
		return self.__projects.pop(project.getName(), None) != None and \
			self.__invoiceControllers.pop(project, None) != None