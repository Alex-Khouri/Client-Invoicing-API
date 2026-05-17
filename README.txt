----------------------------------------
--- REQUIREMENTS ---

* Python 3.10 or greater
* Python libraries:
	- Flask 3.0.0 or greater

----------------------------------------
--- INSTRUCTIONS ---

1) Navigate to "./Source" in your terminal
2) Run either "run.bat" (Windows) or "run.sh" (Linux)
3) Use an endpoint testing tool (e.g. Postman) to evaluate each API endpoint (see 'Testing' section for further information)

----------------------------------------
--- TESTING ---

* The following test data is automatically populated by the TestDataGenerator
* Automated tests are run on application startup to validate test data (results can be seen in console)

TEST DATA:

Users: {
	Username: Staff1
	Password: Password1
	Role: Staff
},
{
	Username: Manager1
	Password: Password1
	Role: Manager
},
Clients: {
	Name: Client1
	Projects: {
		Name: Project1-1
		Invoices: { ID: 1 }, { ID: 2 }
	},
	{
		Name: Project1-2
		Invoices: { ID: 1 }, { ID: 2 }
	}
},
{
	Name: Client2
	Projects: {
		Name: Project2-1
		Invoices: { ID: 1 }, { ID: 2 }
	},
	{
		Name: Project2-2
		Invoices: { ID: 1 }, { ID: 2 }
	}
}

ENDPOINT INPUT EXAMPLES:

----
Login
GET http://127.0.0.1:8080/login?username=Staff1&password=Password1
GET http://127.0.0.1:8080/login?username=Manager1&password=Password1

NB: Subsequent URLs assume that the following session tokens are assigned:
Staff1 (Role = Staff): 1
Manager1 (Role = Manager): 2
----
Logout Session
GET http://127.0.0.1:8080/logout-session?session=1
GET http://127.0.0.1:8080/logout-session?session=2
----
Logout All
GET http://127.0.0.1:8080/logout-all?session=1
GET http://127.0.0.1:8080/logout-all?session=2
----
Client Report
GET http://127.0.0.1:8080/client/Client1?session=2
GET http://127.0.0.1:8080/client/Client2?session=2
----
Client Report (Outstanding Only)
GET http://127.0.0.1:8080/client/Client1?session=2&outstandingOnly=true
GET http://127.0.0.1:8080/client/Client2?session=2&outstandingOnly=true
----
Project Report
GET http://127.0.0.1:8080/client/Client1/project/Project1-1?session=2
GET http://127.0.0.1:8080/client/Client1/project/Project1-2?session=2
GET http://127.0.0.1:8080/client/Client2/project/Project2-1?session=2
GET http://127.0.0.1:8080/client/Client2/project/Project2-2?session=2
----
Invoice Report
GET http://127.0.0.1:8080/client/Client1/project/Project1-1/invoice/1?session=2
GET http://127.0.0.1:8080/client/Client1/project/Project1-1/invoice/2?session=2
GET http://127.0.0.1:8080/client/Client1/project/Project1-2/invoice/1?session=2
GET http://127.0.0.1:8080/client/Client1/project/Project1-2/invoice/2?session=2
GET http://127.0.0.1:8080/client/Client2/project/Project2-1/invoice/1?session=2
GET http://127.0.0.1:8080/client/Client2/project/Project2-1/invoice/2?session=2
GET http://127.0.0.1:8080/client/Client2/project/Project2-2/invoice/1?session=2
GET http://127.0.0.1:8080/client/Client2/project/Project2-2/invoice/2?session=2
----
Delete Invoice
DELETE http://127.0.0.1:8080/client/Client1/project/Project1-1/invoice/1?session=1
DELETE http://127.0.0.1:8080/client/Client1/project/Project1-1/invoice/2?session=1
DELETE http://127.0.0.1:8080/client/Client1/project/Project1-2/invoice/1?session=1
DELETE http://127.0.0.1:8080/client/Client1/project/Project1-2/invoice/2?session=1
DELETE http://127.0.0.1:8080/client/Client2/project/Project2-1/invoice/1?session=1
DELETE http://127.0.0.1:8080/client/Client2/project/Project2-1/invoice/2?session=1
DELETE http://127.0.0.1:8080/client/Client2/project/Project2-2/invoice/1?session=1
DELETE http://127.0.0.1:8080/client/Client2/project/Project2-2/invoice/2?session=1
----
Create Invoice
POST http://127.0.0.1:8080/client/Client1/project/Project1-1/invoice?session=1
POST http://127.0.0.1:8080/client/Client1/project/Project1-2/invoice?session=1
POST http://127.0.0.1:8080/client/Client2/project/Project2-1/invoice?session=1
POST http://127.0.0.1:8080/client/Client2/project/Project2-2/invoice?session=1
----
Adjust Invoice
PATCH http://127.0.0.1:8080/client/Client1/project/Project1-1/invoice/1?session=1&action=adjust&amount=20.50&description=test
PATCH http://127.0.0.1:8080/client/Client1/project/Project1-1/invoice/1?session=2&action=approve
PATCH http://127.0.0.1:8080/client/Client1/project/Project1-1/invoice/1?session=1&action=send
PATCH http://127.0.0.1:8080/client/Client1/project/Project1-1/invoice/1?session=1&action=pay
----

INVOICE ACTION TYPES:
* ADJUST
* DRAFT
* APPROVE
* SEND
* PAY
NB: REPORT, CREATE, and DELETE are specified by HTTP message types (rather than URL arguments)
----------------------------------------