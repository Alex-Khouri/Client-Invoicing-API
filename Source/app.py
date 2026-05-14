from .Globals import *

from .Controller.ClientProjectController import ClientProjectController
from .Controller.InvoiceController import InvoiceController
from .Controller.SessionController import SessionController

from flask import Flask, request

clientProjectController = ClientProjectController()
invoiceController = InvoiceController()
sessionController = SessionController()

app = Flask(__name__)

@app.route("/test", methods=["GET"])
def test():
	return {"item1": 1, "item2": 2, "item3": 3}

# /login?username=text&password=text
@app.route("/login", methods=["GET"])
def login():
	username = request.args.get("username", None)
	password = request.args.get("password", None)
	return 200

# e.g. /logout-session?session=123
@app.route("/logout-session", methods=["GET"])
def logoutSession():
	session = request.args.get("session", None)
	return 200

# e.g. /logout-all?session=123
@app.route("/logout-all", methods=["GET"])
def logoutAll():
	session = request.args.get("session", None)
	return 200

# e.g. /client-name?session=123
@app.route("/client/<string:clientName>", methods=["GET"])
def getClientInvoices(clientName:str):
	session = request.args.get("session", None)
	return 200

# e.g. /client-name/project-name?session=123
@app.route("/client/<string:clientName>/project/<string:projectName>", methods=["GET"])
def getProjectInvoices(clientName:str, projectName:str):
	session = request.args.get("session", None)
	return 200

# e.g. /client-name/project-name/invoice?session=123
@app.route("/client/<string:clientName>/project/<string:projectName>/invoice", methods=["POST"])
def createProjectInvoice(clientName:str, projectName:str):
	session = request.args.get("session", None)
	return 200

# e.g. /client-name/project-name/123?session=456
@app.route("/client/<string:clientName>/project/<string:projectName>/invoice/<int:invoiceID>", methods=["GET"])
def getProjectInvoice(clientName:str, projectName:str, invoiceID:int):
	session = request.args.get("session", None)
	return 200

# e.g. /client-name/project-name/invoice-123?session=456
@app.route("/client/<string:clientName>/project/<string:projectName>/invoice/<int:invoiceID>", methods=["DELETE"])
def deleteProjectInvoice(clientName:str, projectName:str, invoiceID:int):
	session = request.args.get("session", None)
	return 200

# e.g. /client-name/project-name/invoice-123?session=456&action=adjust&adjustmentName=test&adjustmentAmount=20.50
@app.route("/client/<string:clientName>/project/<string:projectName>/invoice/<int:invoiceID>", methods=["PATCH"])
def updateProjectInvoice(clientName:str, projectName:str, invoiceID:int):
	session = request.args.get("session", None)
	action = request.args.get("action", None)
	adjustmentName = request.args.get("adjustmentName", None) # Optional
	adjustmentAmount = request.args.get("adjustmentAmount", None) # Optional
	return 200

app.run(port=APP_PORT, debug=True)