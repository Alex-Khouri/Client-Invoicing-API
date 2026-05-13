from datetime import datetime

from enum import Enum

APP_PORT = 8080

NULL_INVOICE_ID		= 0
MIN_INVOICE_ID		= 1
MAX_INVOICE_ID		= (2 ** 63) - 1	# Maximum positive signed 64-bit value

NULL_SESSION_CODE	= 0
MIN_SESSION_CODE	= 1
MAX_SESSION_CODE	= (2 ** 63) - 1	# Maximum positive signed 64-bit value

class SOURCE(Enum):
	# General
	APP 					= "APP",
	GLOBALS 				= "GLOBALS",
	# Controller
	INVOICE_CONTROLLER		= "INVOICE_CONTROLLER",
	SESSION_CONTROLLER		= "SESSION_CONTROLLER",
	# Model
	INVOICE 				= "INVOICE",
	INVOICE_ADJUSTMENT		= "INVOICE_ADJUSTMENT",
	INVOICE_ENTRY 			= "INVOICE_ENTRY",
	CLIENT 					= "CLIENT",
	PROJECT 				= "PROJECT",
	USER					= "USER"

class INVOICE_ACTION(Enum):
	NULL		= "NULL"
	##############################
	# HTTP: POST
	CREATE		= "CREATE"
	##############################
	# HTTP: DELETE
	DELETE		= "DELETE"
	##############################
	# HTTP: PATCH
	ADJUST		= "ADJUST"
	DRAFT		= "DRAFT"
	APPROVE		= "APPROVE"
	SEND		= "SEND"
	PAY			= "PAY"
	##############################

class INVOICE_ADJUSTMENT(Enum):
	NULL 		= "NULL",
	ADD 		= "ADD",
	REMOVE 		= "REMOVE"

class INVOICE_STATE(Enum):
	NULL 		= "NULL"
	DRAFT 		= "DRAFT"
	APPROVED 	= "APPROVED"
	SENT 		= "SENT"
	PAID 		= "PAID"

class USER_ROLE(Enum):
	NULL 		= "NULL"
	STAFF 		= "STAFF"
	MANAGER 	= "MANAGER"

def LOG(source:SOURCE, message:str):
	print(f"LOG [{source}] [{datetime.now()}]: {message}")

def WARNING(source:SOURCE, message:str):
	print(f"WARNING [{source}] [{datetime.now()}]: {message}")

def ERROR(source:SOURCE, message:str):
	print(f"ERROR [{source}] [{datetime.now()}]: {message}")