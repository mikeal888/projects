# Make set of functions which can be used to log and input inventory.

# Basic objects will have name, price, quantity.

class stock:
# Create stock unit
	def __init__ (self, name, price, quantity):
		self.name = name 		# Name of stock 
		self.price = price		# Total cost of stock
		self.quantity = quantity		# Total quantity of stock

	def add(self, INVENTORY):
		
		if any(n.name == self.name for n in INVENTORY):		# check if already in inventory
			prod = list(filter(lambda x: x.name == self.name, INVENTORY))[0]
			prod.price += self.price
			prod.quantity += self.quantity
		else:
			INVENTORY.append(self)

		print("Added", self.quantity, "units of",  self.name)


