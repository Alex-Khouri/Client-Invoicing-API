from .. import *

class Client:
	name: str
	projects: list

	def __init__(self, name:str):
		self.name = name
		self.projects = []
	
	def getName(self):
		return self.name
	
	def getProjects(self):
		return self.projects
	
	def setName(self, newName:str):
		if newName == "":
			ERROR(SOURCE.CLIENT, "Unable to assign empty name value")
			return

		self.name = newName
	
	def setProjects(self, newProjects:list):
		self.projects = list(newProjects)
	
	def addProject(self, newProject:Project):
		if newProject in self.projects:
			WARNING(SOURCE.CLIENT,\
		   		f"Unable to add {newProject.getName()} to {self.name} client, as project is already contained within client's collection")
			return False
		
		self.projects.append(newProject)
		return True
	
	def removeProject(self, newProject:Project):
		if newProject not in self.projects:
			WARNING(SOURCE.CLIENT,\
		   		f"Unable to remove {newProject.getName()} from {self.name} client, as project isn't contained within current collection")
			return False
		
		self.projects.remove(newProject)
		return True
	
	def clearProjects(self):
		self.projects.clear()