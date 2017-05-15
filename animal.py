class Animal(object):
	"""docstring for Animal"""
	def __init__(self, name):
		self.name = name
		self.health = 100
	def walk(self):
		self.health -= 1
		return self
	def run(self):
		self.health -= 5
		return self
	def displayHealth(self):
		print self.health
		return self

#myanimal = Animal('Cat')

#myanimal.walk().walk().walk().run().run().displayHealth()

#myanimal.walk().walk().walk().run().run().pet().displayHealth()

#myanimal.walk().walk().walk().run().run().fly().displayHealth()