import uuid
class Call(object):
	"""docstring for Call"""
	def __init__(self, name, phonenum, time, reason):
		self.uniqueId = uuid.uuid4()
		self.name = name
		self.phonenum = phonenum
		self.time = time
		self.reason = reason
	def display(self):
		print 'Unique ID: {} \nCaller Name: {} \nCaller Phone Number: {} \nTime: {} \nReason: {}'.format(self.uniqueId, self.name, self.phonenum, self.time, self.reason)
		return self

class CallCenter(object):
	def __init__(self, calls):
		self.calls = calls
		self.queueSize = len(self.calls)
	def add(self, call):
		self.calls.append(call)
		self.queueSize += 1
		return self
	def remove(self):
		self.calls.pop(0)
		self.queueSize -= 1
		return self
	def info(self):
		print 'Queue Length: {}\n'.format(self.queueSize)
		for i in range(0,len(self.calls)):
			print 'Caller Name: {} \nCaller Phone Number: {}\n'.format(self.calls[i].name, self.calls[i].phonenum)	

mycall = Call('Kaan',123124124,'3 AM', 'Bored')
mycall.display()

mycall1 = Call('Bob',455124132,'2 AM', 'Needs help')
mycall1.display()

mycall2 = Call('Jimbo',132131244,'5 PM', 'Prank call')
mycall2.display()

mycall3 = Call('Timmy',187752313,'3 PM', 'Needs help')
mycall3.display()

print

cc = CallCenter([mycall,mycall1,mycall2])
cc.add(mycall3).remove().remove().info()
