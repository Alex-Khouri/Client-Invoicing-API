--- Requirements ---

* Python 3.10 or greater
* Python libraries:
	- Flask 3.0.0 or greater

--- Instructions ---

1) Navigate to "./Source"
2) Run either "run.bat" (Windows) or "run.sh" (Linux)
3) Use an endpoint testing tool (e.g. Postman) to evaluate each API endpoint

Use the following data for testing:
Users:
{
	Username: Staff1
	Password: Password1
	Role: Staff
},
{
	Username: Manager1
	Password: Password1
	Role: Manager
},
Clients:
{
	Name: Client1
	Projects:
	{
		Name: Project1-1
		Invoices:
		{
			ID: TBC
		}
	},
	{
		Name: Project1-2
		Invoices:
		{
			ID: TBC
		}
	}
},
{
	Name: Client2
	Projects:
	{
		Name: Project2-1
		Invoices:
		{
			ID: TBC
		}
	},
	{
		Name: Project2-2
		Invoices:
		{
			ID: TBC
		}
	}
}