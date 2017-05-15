import uuid
class Hospital(object):
	"""docstring for Hospital"""
	def __init__(self, name, capacity):
		self.patients = []
		self.name = name
		self.capacity = capacity
		self.fullBeds = 0
	def admit(self, patient):
		self.patients.append(patient)
		i = 1
		for j in range(0, len(self.patients)):
			print self.patients[j].name, self.patients[j].bedNumber
		# go thru available beds
		while i < self.capacity+1:
			for j in range(0, len(self.patients)):
				if i != self.patients[j].bedNumber:
					patient.bedNumber = i
					break
				i += 1
			else:
				continue
			break
		self.fullBeds += 1
		self.patients = sorted(self.patients, key=lambda self: self.bedNumber)
		print patient.name, 'admitted to', self.name, '...'
		return self
	def discharge(self,patient):
		for element in self.patients:
			if patient.name == element.name:
				element.bedNumber = 0
				self.patients.remove(element)
				self.patients = sorted(self.patients, key=lambda self: self.bedNumber)
				self.fullBeds -= 1
		return self
	def display(self):
		print 'Hospital Name: {} \nHospital Capacity: {}'.format(self.name, self.capacity)
		for element in self.patients:
			string = 'Patient ID: {} \nPatient Name: {} \nPatient Age: {} \nBed Number: {}\nAllergies: '.format(element.id, element.name, element.age, element.bedNumber)
			# add allergies to the string
			for allergy in element.allergies:
				string += allergy + ', '
			# get rid of the last comma
			string = string[:len(string)-2]
			print string
		return self


class Patient(object):
	"""docstring for Patient"""
	def __init__(self, name, age, allergies, bedNumber = None):
		self.id = uuid.uuid4()
		self.name = name
		self.age = age
		self.allergies = allergies
		self.bedNumber = 0

p = Patient('Kaan', 22, ['hayfever', 'peanut allergy', 'dust allergy'])
p1 = Patient('Bob', 45, ['hayfever', 'mosquito allergy'])
p2 = Patient('Jimbo', 66, ['skin allergy', 'pet allergy'])
p3 = Patient('Joel', 23, ['hayfever', 'egg allergy'])
p4 = Patient('Billy', 23, ['hayfever', 'egg allergy'])

h = Hospital('San Jose Hospital', 200)


h.admit(p).admit(p1).admit(p2).discharge(p).admit(p3).admit(p4).display()

