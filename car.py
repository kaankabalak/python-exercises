class Car(object):
	"""docstring for Car"""
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		if price > 10000 :
			self.tax = 0.15
		else :
			self.tax = 0.12

	def display_all(self):
		return 'Price: {} \nSpeed: {}mph \nFuel: {} \nMileage: {}mpg \nTax: {}'.format(self.price, self.speed, self.fuel, self.mileage, self.tax)

mycar = Car(2000, 35, 'Full', 15)
print mycar.display_all(), '\n'

mycar1 = Car(2000, 5, 'Not Full', 105)
print mycar1.display_all(), '\n'

mycar2 = Car(2000, 15, 'Kind of Full', 95)
print mycar2.display_all(), '\n'

mycar3 = Car(2000, 25, 'Full', 25)
print mycar3.display_all(), '\n'

mycar4 = Car(2000, 45, 'Empty', 25)
print mycar4.display_all(), '\n'

mycar5 = Car(2000000, 35, 'Empty', 25)
print mycar5.display_all(), '\n'
