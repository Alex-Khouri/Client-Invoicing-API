class InvoiceController:
	Clients: list
	Projects: list
	Invoices: list
	Adjustments: list
	
	def __init__(self):
		self.Clients = []
		self.Projects = []
		self.Invoices = []
		self.Adjustments = []