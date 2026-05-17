----------------------------------------
--- Requirements ---

* Python 3.10 or greater
* Python libraries:
	- Flask 3.0.0 or greater

----------------------------------------
--- Instructions ---

1) Navigate to "./Source"
2) Run either "run.bat" (Windows) or "run.sh" (Linux)
3) Use an endpoint testing tool (e.g. Postman) to evaluate each API endpoint (see 'Testing' section for further information)

----------------------------------------
--- Testing ---

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

GET http://127.0.0.1:8080/login?username=Staff1&password=Password1
GET http://127.0.0.1:8080/login?username=Manager1&password=Password1
----
GET http://127.0.0.1:8080/logout-session?session=1
GET http://127.0.0.1:8080/logout-session?session=2
----
GET http://127.0.0.1:8080/logout-all?session=1
GET http://127.0.0.1:8080/logout-all?session=2
----
GET http://127.0.0.1:8080/client/Client1?session=2
GET http://127.0.0.1:8080/client/Client2?session=2
----
GET http://127.0.0.1:8080/client/Client1/project/Project1-1?session=2
GET http://127.0.0.1:8080/client/Client1/project/Project1-2?session=2
GET http://127.0.0.1:8080/client/Client2/project/Project2-1?session=2
GET http://127.0.0.1:8080/client/Client2/project/Project2-2?session=2
----
GET http://127.0.0.1:8080/client/Client1/project/Project1-1/invoice/1?session=2
GET http://127.0.0.1:8080/client/Client1/project/Project1-1/invoice/2?session=2
GET http://127.0.0.1:8080/client/Client1/project/Project1-2/invoice/1?session=2
GET http://127.0.0.1:8080/client/Client1/project/Project1-2/invoice/2?session=2
GET http://127.0.0.1:8080/client/Client2/project/Project2-1/invoice/1?session=2
GET http://127.0.0.1:8080/client/Client2/project/Project2-1/invoice/2?session=2
GET http://127.0.0.1:8080/client/Client2/project/Project2-2/invoice/1?session=2
GET http://127.0.0.1:8080/client/Client2/project/Project2-2/invoice/2?session=2
----
DELETE http://127.0.0.1:8080/client/Client1/project/Project1-1/invoice/1?session=1
DELETE http://127.0.0.1:8080/client/Client1/project/Project1-1/invoice/2?session=1
DELETE http://127.0.0.1:8080/client/Client1/project/Project1-2/invoice/1?session=1
DELETE http://127.0.0.1:8080/client/Client1/project/Project1-2/invoice/2?session=1
DELETE http://127.0.0.1:8080/client/Client2/project/Project2-1/invoice/1?session=1
DELETE http://127.0.0.1:8080/client/Client2/project/Project2-1/invoice/2?session=1
DELETE http://127.0.0.1:8080/client/Client2/project/Project2-2/invoice/1?session=1
DELETE http://127.0.0.1:8080/client/Client2/project/Project2-2/invoice/2?session=1
----
POST http://127.0.0.1:8080/client/Client1/project/Project1-1/invoice?session=1
POST http://127.0.0.1:8080/client/Client1/project/Project1-2/invoice?session=1
POST http://127.0.0.1:8080/client/Client2/project/Project2-1/invoice?session=1
POST http://127.0.0.1:8080/client/Client2/project/Project2-2/invoice?session=1
----------------------------------------