class Bike(object):
	"""docstring for bike"""
	def __init__(self, price, max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0
	def displayInfo(self):
		print 'Price: {}, Max Speed: {}, Miles: {}'.format(self.price, self.max_speed, self.miles)
		return self
	def ride(self):
		print 'Riding...'
		self.miles += 10
		return self
	def reverse(self):
		print 'Reversing...'
		# to stop instance from having negative miles
		if self.miles >= 5:
			self.miles -= 5
		return self

mybike = Bike(200, 10)
mybike.ride().ride().ride().reverse().displayInfo()

mybike1 = Bike(100, 7)
mybike1.ride().ride().reverse().reverse().displayInfo()

mybike2 = Bike(150, 9)
mybike2.reverse().reverse().reverse().displayInfo()