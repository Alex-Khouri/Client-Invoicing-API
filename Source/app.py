from .Globals import *

from .Controller.ClientProjectController import ClientProjectController
from .Controller.InvoiceController import InvoiceController
from .Controller.SessionController import SessionController

from flask import Flask, request

clientProjectController = ClientProjectController()
invoiceController = InvoiceController()
sessionController = SessionController()

app = Flask(__name__)

# Get test data
@app.route("/test", methods=["GET"])
def test():
	return {"item1": 1, "item2": 2, "item3": 3}

# /login?username=text&password=text
@app.route("/login", methods=["GET"])
def login():
	username = request.args.get("username", None)
	password = request.args.get("password", None)
	return sessionController.login(username, password)

# e.g. /logout-session?session=123
@app.route("/logout-session", methods=["GET"])
def logoutSession():
	sessionToken = request.args.get("session", None)
	sessionController.logoutSession(sessionToken)
	return 200

# e.g. /logout-all?session=123
@app.route("/logout-all", methods=["GET"])
def logoutAll():
	sessionToken = request.args.get("session", None)
	sessionController.logoutAllSessions(sessionToken)
	return 200

# e.g. /client-name?session=123
@app.route("/client/<string:clientName>", methods=["GET"])
def getClientInvoiceReport(clientName:str):
	sessionToken = request.args.get("session", None)
	if not sessionController.userCanPerformInvoiceAction(sessionToken, INVOICE_ACTION.REPORT):
		return 403
	return 200

# e.g. /client-name/project-name?session=123
@app.route("/client/<string:clientName>/project/<string:projectName>", methods=["GET"])
def getProjectInvoiceReport(clientName:str, projectName:str):
	sessionToken = request.args.get("session", None)
	if not sessionController.userCanPerformInvoiceAction(sessionToken, INVOICE_ACTION.REPORT):
		return 403
	return 200

# e.g. /client-name/project-name/invoice?session=123
@app.route("/client/<string:clientName>/project/<string:projectName>/invoice", methods=["POST"])
def createProjectInvoice(clientName:str, projectName:str):
	sessionToken = request.args.get("session", None)
	if not sessionController.userCanPerformInvoiceAction(sessionToken, INVOICE_ACTION.CREATE):
		return 403
	return 200

# e.g. /client-name/project-name/123?session=456
@app.route("/client/<string:clientName>/project/<string:projectName>/invoice/<int:invoiceID>", methods=["GET"])
def getProjectInvoiceReport(clientName:str, projectName:str, invoiceID:int):
	sessionToken = request.args.get("session", None)
	if not sessionController.userCanPerformInvoiceAction(sessionToken, INVOICE_ACTION.REPORT):
		return 403
	return 200

# e.g. /client-name/project-name/invoice-123?session=456
@app.route("/client/<string:clientName>/project/<string:projectName>/invoice/<int:invoiceID>", methods=["DELETE"])
def deleteProjectInvoice(clientName:str, projectName:str, invoiceID:int):
	sessionToken = request.args.get("session", None)
	if not sessionController.userCanPerformInvoiceAction(sessionToken, INVOICE_ACTION.DELETE):
		return 403
	return 200

# e.g. /client-name/project-name/invoice-123?session=456&action=adjust&adjustmentName=test&adjustmentAmount=20.50
@app.route("/client/<string:clientName>/project/<string:projectName>/invoice/<int:invoiceID>", methods=["PATCH"])
def updateProjectInvoice(clientName:str, projectName:str, invoiceID:int):
	sessionToken = request.args.get("session", None)
	action = request.args.get("action", None)
	adjustmentName = request.args.get("adjustmentName", None) # Optional
	adjustmentAmount = request.args.get("adjustmentAmount", None) # Optional
	if not sessionController.userCanPerformInvoiceAction(sessionToken, INVOICE_ACTION.ADJUST):
		return 403
	return 200

app.run(port=APP_PORT, debug=True)