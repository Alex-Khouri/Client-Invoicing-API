from datetime import datetime
from enum import Enum

class SOURCE(Enum):
	# General
	APP = "APP",
	GLOBALS = "GLOBALS",
	# Controller
	INVOICE_CONTROLLER = "INVOICE_CONTROLLER",
	SESSION_CONTROLLER = "SESSION_CONTROLLER",
	# Model
	ADJUSTMENT = "ADJUSTMENT",
	CLIENT = "CLIENT",
	INVOICE = "INVOICE",
	PROJECT = "PROJECT",
	USER = "USER"
	

class INVOICE_STATE(Enum):
	NULL = "NULL"
	DRAFT = "DRAFT"
	APPROVED = "APPROVED"
	SENT = "SENT"
	PAID = "PAID"

class USER_ROLE(Enum):
	NULL = "NULL"
	STAFF = "STAFF"
	MANAGER = "MANAGER"

def LOG(source:SOURCE, message:str):
	print(f"LOG [{source}] [{datetime.now()}]: {message}")

def WARNING(source:SOURCE, message:str):
	print(f"WARNING [{source}] [{datetime.now()}]: {message}")

def ERROR(source:SOURCE, message:str):
	print(f"ERROR [{source}] [{datetime.now()}]: {message}")