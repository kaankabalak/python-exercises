from animal import Animal
class Dog(Animal):
	"""docstring for Dog"""
	def __init__(self,name):
		super(Dog, self).__init__(name)
		self.health = 150
	def pet(self):
		self.health += 5
		return self

mydog = Dog('Dog')
mydog.walk().walk().walk().run().run().pet().displayHealth()