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

class Store(object) :
	def __init__(self, products, location, owner):
		self.products = []
		for element in products:
			self.products.append(element)
		self.location = location
		self.owner = owner
	def add_product(self, product):
		self.products.append(product)
		return self
	def remove_product(self, productname):
		i = 0
		while i < len(self.products):
			if productname == self.products[i].itemname :
				self.products.pop(i)
				i = i-1	
			i = i+1
		return self
	def inventory(self):
		print 'Store Location: {} \nStore Owner: {} \n'.format(self.location, self.owner)
		print 'Store Inventory:'
		for element in self.products:
			print element.displayInfo(), '\n'
		#print self.products
		#print 'Price: ${} \nItem Name: {} \nWeight: {} lb \nBrand: {} \nCost: ${} \nStatus: {}'.format(element.price, element.itemname, element.weight, element.brand, element.cost, element.status)
		return self

myproduct = Product(5, 'Thermos', 1, 'contigo', 2)
myproduct.displayInfo(), '\n'

myproduct1 = Product(5, 'Thermos', 1, 'contigo', 2)
myproduct1.sell().displayInfo(), '\n'

myproduct2 = Product(5, 'Thermos', 1, 'contigo', 2)
myproduct2.sell().returnItem("Didn't like it", True).displayInfo(), '\n'

myproduct3 = Product(5, 'Thermos', 1, 'contigo', 2)
myproduct3.sell().returnItem("Defective", False).displayInfo(), '\n'

myproduct4 = Product(5, 'Thermos', 1, 'contigo', 2)
myproduct4.sell().returnItem("Defective", True).displayInfo(), '\n'

myproduct5 = Product(5, 'Thermos', 1, 'contigo', 2)
myproduct5.sell().returnItem("Wants to buy a new thermos", False).displayInfo(), '\n'

products = [myproduct, myproduct1, myproduct2, myproduct3, myproduct4, myproduct5]

mystore = Store(products, 'San Jose', 'Kaan')

newproduct = Product(2, 'Drink', 0.33, 'Mountain Dew', 0.4)

mystore.add_product(newproduct).inventory()

mystore.remove_product('Thermos').inventory()




