# Start a new inventory but make make inventory class and stock class

class stock:
	# Create a stock object 
	def __init__(self, name, price, quantity):
		self.name = name				# Name of item
		self.price = price				# Total price of items
		self.quantity = quantity		# Total quantity of items


class inventory:
	# create inventory object
	def __init__(self, name, stock):
		self.name = name 				# Name of inventory
		self.stock = {} 				# Stock in inventory

	def add(self, ITEM):
		# Add stock to inventory
		self.stock[ITEM.name] = ITEM
