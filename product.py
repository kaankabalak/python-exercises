class Product(object):
	"""docstring for Product"""
	def __init__(self, price, itemname, weight, brand, cost):
		self.price = price
		self.itemname = itemname
		self.weight = weight
		self.brand = brand
		self.cost = cost
		self.status = 'For Sale'
	def sell(self):
		self.status = 'Sold'
		return self
	def addTax(self, tax):
		self.price += tax
		return self
	def returnItem(self, reason, isReturnedInBox):
		if isReturnedInBox == True:
			self.status = 'For Sale'
		else:
			self.status = 'Used'
			self.price = self.price * 4/5
		if reason == 'Defective':
			self.status = 'Defective'
			self.price = 0
		return self
	def displayInfo(self):
		return 'Price: ${} \nItem Name: {} \nWeight: {} lb \nBrand: {} \nCost: ${} \nStatus: {}'.format(self.price, self.itemname, self.weight, self.brand, self.cost, self.status)

myproduct = Product(5, 'Thermos', 1, 'contigo', 2)
print myproduct.displayInfo(), '\n'

myproduct = Product(5, 'Thermos', 1, 'contigo', 2)
print myproduct.sell().displayInfo(), '\n'

myproduct = Product(5, 'Thermos', 1, 'contigo', 2)
print myproduct.sell().returnItem("Didn't like it", True).displayInfo(), '\n'

myproduct = Product(5, 'Thermos', 1, 'contigo', 2)
print myproduct.sell().returnItem("Defective", False).displayInfo(), '\n'

myproduct = Product(5, 'Thermos', 1, 'contigo', 2)
print myproduct.sell().returnItem("Defective", True).displayInfo(), '\n'

myproduct = Product(5, 'Thermos', 1, 'contigo', 2)
print myproduct.sell().returnItem("Wants to buy a new thermos", False).displayInfo(), '\n'