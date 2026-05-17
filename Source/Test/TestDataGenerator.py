from ..Globals import *

from ..Controller.ClientProjectController import ClientProjectController
from ..Controller.UserAccessController import UserAccessController

from ..Model.Client import Client
from ..Model.Invoice.Invoice import Invoice
from ..Model.Invoice.InvoiceAdjustment import InvoiceAdjustment
from ..Model.Invoice.InvoiceEntry import InvoiceEntry
from ..Model.Project import Project
from ..Model.User import User

def TEST(condition:bool, conditionString:str):
	result = "PASS" if condition else "FAIL"
	print(f"TEST: {conditionString} - {result}")
	return condition

class TestDataGenerator:
	__clientProjectController:ClientProjectController
	__userAccessController:UserAccessController

	def __init__(self, clientProjectController:ClientProjectController,
			  				userAccessController:UserAccessController):
		self.__clientProjectController = clientProjectController
		self.__userAccessController = userAccessController
	
	def initialiseTestData(self):
		print("----------------------------------------\n>> RUNNING TESTS...\n")
		failures = 0
		try:
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
			failures += 0 if TEST(client1 is not None, f"client1 is not None") else 1
			failures += 0 if TEST(client2 is not None, f"client2 is not None") else 1
			failures += 0 if TEST(client1.getName() == clientName1, f"client1.getName() == {clientName1}") else 1
			failures += 0 if TEST(client2.getName() == clientName2, f"client2.getName() == {clientName2}") else 1
			print("----------")

			# Initialise projects
			projectName1_1 = "Project1-1"
			projectName1_2 = "Project1-2"
			projectName2_1 = "Project2-1"
			projectName2_2 = "Project2-2"
			project1_1 = self.__clientProjectController.createProject(clientName1, projectName1_1)
			project1_2 = self.__clientProjectController.createProject(clientName1, projectName1_2)
			project2_1 = self.__clientProjectController.createProject(clientName2, projectName2_1)
			project2_2 = self.__clientProjectController.createProject(clientName2, projectName2_2)
			failures += 0 if TEST(project1_1 is not None, f"project1_1 is not None") else 1
			failures += 0 if TEST(project1_2 is not None, f"project1_2 is not None") else 1
			failures += 0 if TEST(project2_1 is not None, f"project2_1 is not None") else 1
			failures += 0 if TEST(project2_2 is not None, f"project2_2 is not None") else 1
			failures += 0 if TEST(project1_1.getName() == projectName1_1,
						 			f"project1_1.getName() == {projectName1_1}") else 1
			failures += 0 if TEST(project1_2.getName() == projectName1_2,
						 			f"project1_2.getName() == {projectName1_2}") else 1
			failures += 0 if TEST(project2_1.getName() == projectName2_1,
						 			f"project2_1.getName() == {projectName2_1}") else 1
			failures += 0 if TEST(project2_2.getName() == projectName2_2,
						 			f"project2_2.getName() == {projectName2_2}") else 1
			print("----------")

			# Initialise invoices
			invoice1_1_1 = self.__clientProjectController.createInvoice(project1_1)
			invoice1_1_2 = self.__clientProjectController.createInvoice(project1_1)
			invoice1_2_1 = self.__clientProjectController.createInvoice(project1_2)
			invoice1_2_2 = self.__clientProjectController.createInvoice(project1_2)
			invoice2_1_1 = self.__clientProjectController.createInvoice(project2_1)
			invoice2_1_2 = self.__clientProjectController.createInvoice(project2_1)
			invoice2_2_1 = self.__clientProjectController.createInvoice(project2_2)
			invoice2_2_2 = self.__clientProjectController.createInvoice(project2_2)
			
			failures += 0 if TEST(invoice1_1_1 is not None, f"invoice1_1_1 is not None") else 1
			failures += 0 if TEST(invoice1_1_2 is not None, f"invoice1_1_2 is not None") else 1
			failures += 0 if TEST(invoice1_2_1 is not None, f"invoice1_2_1 is not None") else 1
			failures += 0 if TEST(invoice1_2_2 is not None, f"invoice1_2_2 is not None") else 1
			failures += 0 if TEST(invoice2_1_1 is not None, f"invoice2_1_1 is not None") else 1
			failures += 0 if TEST(invoice2_1_2 is not None, f"invoice2_1_2 is not None") else 1
			failures += 0 if TEST(invoice2_2_1 is not None, f"invoice2_2_1 is not None") else 1
			failures += 0 if TEST(invoice2_2_2 is not None, f"invoice2_2_2 is not None") else 1

			failures += 0 if TEST(invoice1_1_1.getID() == 1, f"invoice1_1_1.getID() == 1") else 1
			failures += 0 if TEST(invoice1_1_2.getID() == 2, f"invoice1_1_2.getID() == 2") else 1
			failures += 0 if TEST(invoice1_2_1.getID() == 1, f"invoice1_2_1.getID() == 1") else 1
			failures += 0 if TEST(invoice1_2_2.getID() == 2, f"invoice1_2_2.getID() == 2") else 1
			failures += 0 if TEST(invoice2_1_1.getID() == 1, f"invoice2_1_1.getID() == 1") else 1
			failures += 0 if TEST(invoice2_1_2.getID() == 2, f"invoice2_1_2.getID() == 2") else 1
			failures += 0 if TEST(invoice2_2_1.getID() == 1, f"invoice2_2_1.getID() == 1") else 1
			failures += 0 if TEST(invoice2_2_2.getID() == 2, f"invoice2_2_2.getID() == 2") else 1
		
		except Exception as e:
			ERROR(SOURCE.TEST_DATA_GENERATOR, f"Tests failed with the following error:\n{e}")
		finally:
			print(f"\n>> TESTS COMPLETED! Total Failures: {failures}\n----------------------------------------")