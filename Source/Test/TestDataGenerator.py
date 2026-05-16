from ..Globals import *

from ..Controller.ClientProjectController import ClientProjectController
from ..Controller.UserAccessController import UserAccessController

from ..Model.Client import Client
from ..Model.Invoice.Invoice import Invoice
from ..Model.Invoice.InvoiceAdjustment import InvoiceAdjustment
from ..Model.Invoice.InvoiceEntry import InvoiceEntry
from ..Model.Project import Project
from ..Model.User import User

class TestDataGenerator:
	__clientProjectController:ClientProjectController
	__userAccessController:UserAccessController

	def __init__(self, clientProjectController:ClientProjectController,
			  				userAccessController:UserAccessController):
		self.__clientProjectController = clientProjectController
		self.__userAccessController = userAccessController
	
	def initialiseTestData(self):
		# TODO: Finish this

		# Initialise user accounts
		user1Username = "Staff1"
		user1Password = "Password1"
		user1Role = USER_ROLE.STAFF
		user2Username = "Manager1"
		user2Password = "Password1"
		user2Role = USER_ROLE.MANAGER
		self.__userAccessController.register(user1Username, user1Password, user1Role)
		self.__userAccessController.register(user2Username, user2Password, user2Role)

		# Initialise clients
		clientName1 = "Client1"
		clientName2 = "Client2"
		client1 = self.__clientProjectController.createClient(clientName1)
		client2 = self.__clientProjectController.createClient(clientName2)

		# Initialise projects
		projectName1_1 = "Project1-1"
		projectName1_2 = "Project1-2"
		projectName2_1 = "Project2-1"
		projectName2_2 = "Project2-2"
		project1_1 = self.__clientProjectController.createClient(projectName1_1)
		project1_2 = self.__clientProjectController.createClient(projectName1_2)
		project2_1 = self.__clientProjectController.createClient(projectName2_1)
		project2_2 = self.__clientProjectController.createClient(projectName2_2)

		# Initialise invoices

		# Initialise invoice adjustments

		# Apply invoice adjustments (to generate invoice entries)
		pass