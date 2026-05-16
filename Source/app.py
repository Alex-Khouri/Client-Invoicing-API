from .Globals import *

from .Controller.ClientProjectController import ClientProjectController
from .Controller.UserAccessController import UserAccessController
from .Test.TestDataGenerator import TestDataGenerator

from flask import Flask, request

clientProjectController = ClientProjectController()
userAccessController = UserAccessController()

# TODO: Un-comment these lines once test data is ready to use
# testDataGenerator = TestDataGenerator(clientProjectController, userAccessController)
# testDataGenerator.initialiseTestData()

app = Flask(__name__)

# Get test data
@app.route("/test", methods=["GET"])
def test():
	return {"item1": 1, "item2": 2, "item3": 3}

# /register?username=text&password=text&role=text
@app.route("/register", methods=["POST"])
def register():
	username = request.args.get("username", None)
	password = request.args.get("password", None)
	userRole = parseUserRole(request.args.get("role", None))
	if userAccessController.register(username, password, userRole):
		return 201
	else:
		return 400

# /login?username=text&password=text
@app.route("/login", methods=["GET"])
def login():
	username = request.args.get("username", None)
	password = request.args.get("password", None)
	return userAccessController.login(username, password)	# Session token (integer)

# e.g. /logout-session?session=123
@app.route("/logout-session", methods=["GET"])
def logoutSession():
	sessionToken = parseSessionToken(request.args.get("session", None))

	if userAccessController.getUserFromToken(sessionToken) == None:
		return 401

	userAccessController.logoutSession(sessionToken)
	return 200

# e.g. /logout-all?session=123
@app.route("/logout-all", methods=["GET"])
def logoutAll():
	sessionToken = parseSessionToken(request.args.get("session", None))

	if userAccessController.getUserFromToken(sessionToken) == None:
		return 401

	userAccessController.logoutAllSessions(sessionToken)
	return 200

# e.g. /client-name?session=123&outstandingOnly=true
@app.route("/client/<string:clientName>", methods=["GET"])
def getClientReport(clientName:str):
	sessionToken = parseSessionToken(request.args.get("session", None))
	outstandingOnly = request.args.get("outstandingOnly", "false").lower() == "true"

	if userAccessController.getUserFromToken(sessionToken) == None:
		return 401

	if not userAccessController.userCanPerformInvoiceAction(sessionToken, INVOICE_ACTION.REPORT):
		return 403
	
	client = clientProjectController.getClient(clientName)
	if client == None:
		return 404
	
	clientReport = {
		clientName: {}
	}
	for project in client.getProjects():
		projectName = project.getName()
		clientReport[clientName][projectName] = {}
		for invoice in project.getInvoices():
			if outstandingOnly and invoice.getState() != INVOICE_STATE.SENT:
				pass
			invoiceTitle = invoice.getTitle()
			clientReport[clientName][projectName][invoiceTitle] = []
			for entry in invoice.getEntries():
				clientReport[clientName][projectName][invoiceTitle].append(f"{entry}")

	return clientReport		# Dictionary (containing report data)

# e.g. /client-name/project-name?session=123&outstandingOnly=true
@app.route("/client/<string:clientName>/project/<string:projectName>", methods=["GET"])
def getProjectReport(clientName:str, projectName:str):
	sessionToken = parseSessionToken(request.args.get("session", None))
	outstandingOnly = request.args.get("outstandingOnly", "false").lower() == "true"

	if userAccessController.getUserFromToken(sessionToken) == None:
		return 401

	if not userAccessController.userCanPerformInvoiceAction(sessionToken, INVOICE_ACTION.REPORT):
		return 403
	
	client = clientProjectController.getClient(clientName)
	if client == None:
		return 404
	
	project = client.getProject(projectName)
	if (project == None):
		return 404
	
	projectReport = {
		clientName: {
			projectName: {}
		}
	}
	for invoice in project.getInvoices():
		if outstandingOnly and invoice.getState() != INVOICE_STATE.SENT:
				pass
		invoiceTitle = invoice.getTitle()
		projectReport[clientName][projectName][invoiceTitle] = []
		for entry in invoice.getEntries():
			projectReport[clientName][projectName][invoiceTitle].append(f"{entry}")

	return projectReport	# Dictionary (containing report data)

# e.g. /client-name/project-name/invoice?session=123
@app.route("/client/<string:clientName>/project/<string:projectName>/invoice", methods=["POST"])
def createProjectInvoice(clientName:str, projectName:str):
	sessionToken = parseSessionToken(request.args.get("session", None))

	if userAccessController.getUserFromToken(sessionToken) == None:
		return 401

	if not userAccessController.userCanPerformInvoiceAction(sessionToken, INVOICE_ACTION.CREATE):
		return 403
	
	client = clientProjectController.getClient(clientName)
	if client == None:
		return 404
	
	project = client.getProject(projectName)
	if project == None:
		return 404
	
	invoiceController = clientProjectController.getInvoiceController(project)
	if invoiceController == None:
		return 500	# Indicates internal mismanagement of invoice controllers for projects
	
	return invoiceController.createInvoice(project).getID()		# New invoice ID (integer)

# e.g. /client-name/project-name/123?session=456
@app.route("/client/<string:clientName>/project/<string:projectName>/invoice/<int:invoiceID>", methods=["GET"])
def getInvoiceReport(clientName:str, projectName:str, invoiceID:int):
	sessionToken = parseSessionToken(request.args.get("session", None))

	if userAccessController.getUserFromToken(sessionToken) == None:
		return 401

	if not userAccessController.userCanPerformInvoiceAction(sessionToken, INVOICE_ACTION.REPORT):
		return 403
	
	client = clientProjectController.getClient(clientName)
	if client == None:
		return 404
	
	project = client.getProject(projectName)
	if project == None:
		return 404
	
	invoice = project.getInvoice(invoiceID)
	if invoice == None:
		return 404

	invoiceTitle = invoice.getTitle()
	invoiceReport = {
		clientName: {
			projectName: {
				invoiceTitle: []
			}
		}
	}
	for entry in invoice.getEntries():
		invoiceReport[clientName][projectName][invoiceTitle].append(f"{entry}")

	return invoiceReport	# Dictionary (containing report data)

# e.g. /client-name/project-name/invoice-123?session=456
@app.route("/client/<string:clientName>/project/<string:projectName>/invoice/<int:invoiceID>", methods=["DELETE"])
def deleteProjectInvoice(clientName:str, projectName:str, invoiceID:int):
	sessionToken = parseSessionToken(request.args.get("session", None))

	if userAccessController.getUserFromToken(sessionToken) == None:
		return 401

	if not userAccessController.userCanPerformInvoiceAction(sessionToken, INVOICE_ACTION.DELETE):
		return 403
	
	client = clientProjectController.getClient(clientName)
	if client == None:
		return 404
	
	project = client.getProject(projectName)
	if project == None:
		return 404
	
	invoiceController = clientProjectController.getInvoiceController(project)
	if invoiceController == None:
		return 500	# Indicates internal mismanagement of invoice controllers for projects
	
	if invoiceController.deleteInvoice(invoiceID):
		return 204
	else:
		return 400

# e.g. /client-name/project-name/invoice-123?session=456&action=adjust&amount=20.50&description=test
@app.route("/client/<string:clientName>/project/<string:projectName>/invoice/<int:invoiceID>", methods=["PATCH"])
def adjustProjectInvoice(clientName:str, projectName:str, invoiceID:int):
	sessionToken = parseSessionToken(request.args.get("session", None))
	action = parseInvoiceAction(request.args.get("action", None))
	amount = parseAdjustmentAmount(request.args.get("amount", None)) # Optional
	description = request.args.get("description", None) # Optional

	user = userAccessController.getUserFromToken(sessionToken)
	if user == None:
		return 401

	if not userAccessController.userCanPerformInvoiceAction(sessionToken, action):
		return 403

	client = clientProjectController.getClient(clientName)
	if client == None:
		return 404
	
	project = client.getProject(projectName)
	if project == None:
		return 404
	
	invoice = project.getInvoice(invoiceID)
	if invoice == None:
		return 404
	
	invoiceController = clientProjectController.getInvoiceController(project)
	if invoiceController == None:
		return 500	# Indicates internal mismanagement of invoice controllers for projects
	
	if invoiceController.adjustInvoice(user, invoice, action, amount, description):
		return 200
	else:
		return 400

app.run(port=APP_PORT, debug=True)