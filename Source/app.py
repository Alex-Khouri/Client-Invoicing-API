from .Globals import *

from .Controller.ClientProjectController import ClientProjectController
from .Controller.InvoiceController import InvoiceController
from .Controller.UserAccessController import UserAccessController 

from flask import Flask, request

clientProjectController = ClientProjectController()
userAccessController = UserAccessController()

# TODO: Initialise test data

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
	roleString = request.args.get("role", None)
	userAccessController.register(username, password, roleString)
	return 201

# /login?username=text&password=text
@app.route("/login", methods=["GET"])
def login():
	username = request.args.get("username", None)
	password = request.args.get("password", None)
	return userAccessController.login(username, password)

# e.g. /logout-session?session=123
@app.route("/logout-session", methods=["GET"])
def logoutSession():
	sessionToken = request.args.get("session", None)
	userAccessController.logoutSession(sessionToken)
	return 200

# e.g. /logout-all?session=123
@app.route("/logout-all", methods=["GET"])
def logoutAll():
	sessionToken = request.args.get("session", None)
	userAccessController.logoutAllSessions(sessionToken)
	return 200

# e.g. /client-name?session=123
@app.route("/client/<string:clientName>", methods=["GET"])
def getClientReport(clientName:str):
	sessionToken = request.args.get("session", None)
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
			invoiceTitle = invoice.getTitle()
			clientReport[clientName][projectName][invoiceTitle] = []
			for entry in invoice.getEntries():
				clientReport[clientName][projectName][invoiceTitle].append(f"{entry}")

	return clientReport

# e.g. /client-name/project-name?session=123
@app.route("/client/<string:clientName>/project/<string:projectName>", methods=["GET"])
def getProjectReport(clientName:str, projectName:str):
	sessionToken = request.args.get("session", None)
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
		invoiceTitle = invoice.getTitle()
		projectReport[clientName][projectName][invoiceTitle] = []
		for entry in invoice.getEntries():
			projectReport[clientName][projectName][invoiceTitle].append(f"{entry}")

	return projectReport

# e.g. /client-name/project-name/invoice?session=123
@app.route("/client/<string:clientName>/project/<string:projectName>/invoice", methods=["POST"])
def createProjectInvoice(clientName:str, projectName:str):
	sessionToken = request.args.get("session", None)
	if not userAccessController.userCanPerformInvoiceAction(sessionToken, INVOICE_ACTION.CREATE):
		return 403
	return 200

# e.g. /client-name/project-name/123?session=456
@app.route("/client/<string:clientName>/project/<string:projectName>/invoice/<int:invoiceID>", methods=["GET"])
def getInvoiceReport(clientName:str, projectName:str, invoiceID:int):
	sessionToken = request.args.get("session", None)
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

	return invoiceReport

# e.g. /client-name/project-name/invoice-123?session=456
@app.route("/client/<string:clientName>/project/<string:projectName>/invoice/<int:invoiceID>", methods=["DELETE"])
def deleteProjectInvoice(clientName:str, projectName:str, invoiceID:int):
	sessionToken = request.args.get("session", None)
	if not userAccessController.userCanPerformInvoiceAction(sessionToken, INVOICE_ACTION.DELETE):
		return 403
	return 200

# e.g. /client-name/project-name/invoice-123?session=456&action=adjust&adjustmentName=test&adjustmentAmount=20.50
@app.route("/client/<string:clientName>/project/<string:projectName>/invoice/<int:invoiceID>", methods=["PATCH"])
def adjustProjectInvoice(clientName:str, projectName:str, invoiceID:int):
	sessionToken = request.args.get("session", None)
	action = request.args.get("action", None)
	adjustmentName = request.args.get("adjustmentName", None) # Optional
	adjustmentAmount = request.args.get("adjustmentAmount", None) # Optional
	if not userAccessController.userCanPerformInvoiceAction(sessionToken, INVOICE_ACTION.ADJUST):
		return 403
	return 200

app.run(port=APP_PORT, debug=True)