from .. import *

class Client:
	__name: str
	__projects: list[Project]

	def __init__(self, name:str):
		self.__name = name
		self.__projects = []
	
	def getName(self):
		return self.__name
	
	def getProjects(self):
		return self.__projects
	
	def setName(self, newName:str):
		if newName == "":
			ERROR(SOURCE.CLIENT, "Unable to assign empty name value")
			return False

		self.__name = newName
		return True
	
	def setProjects(self, newProjects:list[Project]):
		self.__projects = list(newProjects)
	
	def addProject(self, newProject:Project):
		if newProject in self.__projects:
			WARNING(SOURCE.CLIENT,\
		   		f"Unable to add {newProject.getName()} to {self.__name} client, as project is already contained within client's collection")
			return False
		
		self.__projects.append(newProject)
		return True
	
	def removeProject(self, newProject:Project):
		if newProject not in self.__projects:
			WARNING(SOURCE.CLIENT,\
		   		f"Unable to remove {newProject.getName()} from {self.__name} client, as project isn't contained within current collection")
			return False
		
		self.__projects.remove(newProject)
		return True
	
	def clearProjects(self):
		self.__projects.clear()