from datetime import datetime

from enum import Enum

APP_PORT = 8080

DEFAULT_INVOICE_ENTRY_AMOUNT		= 0.0
DEFAULT_INVOICE_ENTRY_DESCRIPTION	= ""

EMPTY_STRING		= ""

NULL_INVOICE_ID		= 0
MIN_INVOICE_ID		= 1
MAX_INVOICE_ID		= (2 ** 63) - 1	# Maximum positive signed 64-bit value

NULL_SESSION_TOKEN	= 0
MIN_SESSION_TOKEN	= 1
MAX_SESSION_TOKEN	= (2 ** 63) - 1	# Maximum positive signed 64-bit value

class SOURCE(Enum):
	# General
	APP 						= "APP",
	GLOBALS 					= "GLOBALS"
	# Controller
	CLIENT_PROJECT_CONTROLLER	= "CLIENT_PROJECT_CONTROLLER"
	INVOICE_CONTROLLER			= "INVOICE_CONTROLLER"
	USER_ACCESS_CONTROLLER		= "USER_ACCESS_CONTROLLER"
	# Model
	INVOICE 					= "INVOICE"
	INVOICE_ADJUSTMENT			= "INVOICE_ADJUSTMENT"
	INVOICE_ENTRY 				= "INVOICE_ENTRY"
	CLIENT 						= "CLIENT"
	PROJECT 					= "PROJECT"
	USER						= "USER"

# !!! IMPORTANT: All enum values MUST be upper-case (as this is relied upon by parsing functions)
class INVOICE_ACTION(Enum):
	NULL		= "NULL"
	##############################
	# HTTP: GET
	REPORT		= "REPORT"
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

class INVOICE_ENTRY(Enum):
	NULL 		= "NULL"
	ADD 		= "ADD"		# Add entry
	REMOVE 		= "REMOVE"	# Remove entry (implementation TBC)

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

# LOGGING
def LOG(source:SOURCE, message:str):
	print(f"LOG [{source}] [{datetime.now()}]: {message}")

def WARNING(source:SOURCE, message:str):
	print(f"WARNING [{source}] [{datetime.now()}]: {message}")

def WARNING_IF(condition:bool, source:SOURCE, message:str):
	if condition:
		print(f"WARNING [{source}] [{datetime.now()}]: {message}")

def ERROR(source:SOURCE, message:str):
	print(f"ERROR [{source}] [{datetime.now()}]: {message}")

def ERROR_IF(condition:bool, source:SOURCE, message:str):
	if condition:
		print(f"ERROR [{source}] [{datetime.now()}]: {message}")

# HELPER FUNCTIONS
def parseSessionToken(tokenString:str):
	try:
		return int(tokenString)
	except ValueError:
		return NULL_SESSION_TOKEN

def parseAdjustmentAmount(amountString:str):
	try:
		return float(amountString)
	except ValueError:
		return DEFAULT_INVOICE_ENTRY_AMOUNT

def parseInvoiceAction(actionString:str):
	try:
		return INVOICE_ACTION[actionString.upper()]
	except KeyError:
		return INVOICE_ACTION.NULL

def parseUserRole(roleString:str):
	try:
		return USER_ROLE[roleString.upper()]
	except KeyError:
		return USER_ROLE.NULL