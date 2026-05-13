from .Globals import *

from .Controller.InvoiceController import InvoiceController
from .Controller.SessionController import SessionController

from flask import Flask, request

invoiceController = InvoiceController()
sessionController = SessionController()

app = Flask(__name__)

# TODO!: Finish implementing endpoints

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
@app.route("/<str:clientName>", methods=["GET"])
def invoiceAction():
	session = request.args.get("session", None)
	return 200

# e.g. /client-name/project-name?session=123
@app.route("/<str:clientName>/<str:projectName>", methods=["GET"])
def invoiceAction():
	session = request.args.get("session", None)
	return 200

# e.g. /client-name/project-name/invoice?session=123
@app.route("/<str:clientName>/<str:projectName>/invoice", methods=["POST"])
def invoiceAction():
	session = request.args.get("session", None)
	return 200

# e.g. /client-name/project-name/123?session=456
@app.route("/<str:clientName>/<str:projectName>/<int:invoiceID>", methods=["GET"])
def invoiceAction():
	session = request.args.get("session", None)
	return 200

# e.g. /client-name/project-name/123?session=456
@app.route("/<str:clientName>/<str:projectName>/<int:invoiceID>", methods=["DELETE"])
def invoiceAction():
	session = request.args.get("session", None)
	return 200

# e.g. /client-name/project-name/123?session=456&action=adjust&adjustmentName=test&adjustmentAmount=20.50
@app.route("/<str:clientName>/<str:projectName>/<int:invoiceID>", methods=["PATCH"])
def invoiceAction():
	session = request.args.get("session", None)
	action = request.args.get("action", None)
	adjustmentName = request.args.get("adjustmentName", None) # Optional
	adjustmentAmount = request.args.get("adjustmentAmount", None) # Optional
	return 200

app.run(port=APP_PORT, debug=True)