# Start a new inventory but make make inventory class and stock class
# Inventory must take stock objects 

class stock:
	# Create a stock object 
	def __init__(self, name, price, quantity):
		self.name = name				# Name of item
		self.price = price				# Total price of items
		self.quantity = quantity		# Total quantity of items


class inventory(dict):
	# create a dictionary object.
	# This does no require any initialisation.
	# Only these dictionary objects will inherit the methods defined below

	def add(self, id, val):
		
		# Add contents to inventory

		if id in self.keys():
			self[id] += val
			print('Added', val, 'units of', id)
			print('Total units of', id, '=', self[id])
		else:
			self[id] = val
			print('Added', val, 'units of', id)

	def remove(self, id, val):

		# Remove contents from inventory
		
		if id in self.keys():
			self[id] -= val
			print('Removed', val, 'units of', id)
			print('Total units of', id, '=', self[id])
		else:
			print(id, 'not in inventory')

	def items(self):

		# Print items in inventory
		
		print('item', 'units')
		print()
		for index in self.keys():
			print(index, self[index])	
