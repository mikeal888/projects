# Start a new inventory but make make inventory class and stock class
# Inventory must take stock objects 

class stock:

	# Create a stock object 

	def __init__(self, name, price, quantity):
		self.name = name				# Name of item
		self.price = price				# Total price of items
		self.quantity = quantity		# Total quantity of items


class inventory(dict):
	
	# create a dictionary object which takes stock objects as values
	# This does no require any initialisation.
	# Only these dictionary objects will inherit the methods defined below

	def add(self, id):
		
		# Add contents to inventory

		if id.name in self.keys():
			self[id.name].price += id.price
			self[id.name].quantity += id.quantity
			print('Added', id.quantity, 'units of', id.name)
			print('Total units of', id.name, '=', self[id.name].quantity)
			print('Total value of', id.name, '=', '$',self[id.name].price)
		else:
			self[id.name] = id
			print('Added', id.quantity, 'units of', id.name)
			print('Total value of', id.name, '=', '$',self[id.name].price)

	def remove(self, id, val):

		# Remove contents from inventory
		
		if id.name in self.keys():
			self[id.name].price -= id.price
			self[id.name].quantity -= id.quantity
			print('Removed', id.quantity, 'units of', id.name)
			print('Total units of', id.name, '=', self[id.name].quantity)
			print('Total value of', id.name, '=', '$',self[id.name].price)
		else:
			print(id.name, 'not in inventory')

	def items(self):

		# Print items in inventory

		for index in self.keys():
			print(index, self[index].quantity)	

	def summary(self):

		# Make summary text of inventory

		length = len(self)
		total = 0
		for index in self.values():
			total += index.price

		print('Total value of inventory = $', total)
		print('Items in inventory are:')
		self.items()

# Note: When object a = stock(...) is added to inventory inventory.add(a), the object that is added to the dictionary is the same object as a. Hence a now equals a.price/quantity += a.price/quantity. 