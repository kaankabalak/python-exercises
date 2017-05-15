class MathDojo(object):
	"""docstring for MathDojo"""
	def __init__(self):
		self.result = 0
	def add(self,*num):
		for i in range(0, len(num)):
			if isinstance(num[i],int) or isinstance(num[i],float):
				self.result += num[i]
			elif isinstance(num[i],list):
				for j in range(0, len(num[i])):
					self.result += num[i][j]
			elif isinstance(num[i],tuple):
				for k in range(0, len(num[i])):
					self.result += num[i][k]		
		return self
	def subtract(self, *num):
		for i in range(0, len(num)):
			if isinstance(num[i],int) or isinstance(num[i],float):
				self.result -= num[i]
			elif isinstance(num[i],list):
				for j in range(0, len(num[i])):
					self.result -= num[i][j]
			elif isinstance(num[i],tuple):
				for k in range(0, len(num[i])):
					self.result -= num[i][k]	
		return self

md = MathDojo().add(2).add(2,5).subtract(3,2).result
print md

md1 = MathDojo().add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).subtract((3,7,5,5)).result
print md1