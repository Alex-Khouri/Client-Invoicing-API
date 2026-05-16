from ..Globals import *

from ..Model.Project import Project

class Client:
	__name: str
	__projects: dict[str, Project]

	def __init__(self, name:str):
		self.__name = name
		self.__projects = {}
	
	def getName(self):
		return self.__name

	def getProjects(self):
		return self.__projects.values()
	
	def getProject(self, name:str):
		return self.__projects.get(name, None)
	
	def setName(self, newName:str):
		if newName == "":
			ERROR(SOURCE.CLIENT, "Unable to assign empty name value")
			return False

		self.__name = newName
		return True
	
	def setProjects(self, newProjects:list[Project]):
		self.__projects.clear()
		for project in newProjects:
			self.__projects[project.getName()] = project
	
	def addProject(self, newProject:Project):
		if newProject in self.__projects.values():
			WARNING(SOURCE.CLIENT,
		   		f"Unable to add {newProject.getName()} to {self.__name} client, as project is already contained within client's collection")
			return False
		
		self.__projects[newProject.getName()] = newProject
		return True
	
	def removeProject(self, project:Project):
		success = self.__projects.pop(project.getName(), None) != None
		WARNING_IF(not success,
			SOURCE.CLIENT,
			f"Unable to remove {project.getName()} from {self.__name} client, as project isn't contained within current collection")
		return success