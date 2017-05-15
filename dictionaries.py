def makeAndReadDict(keys, values):
	person = zip(keys, values)
	person_dict = dict(person)
	print 'My name is', person_dict['name']
	print 'My age is', person_dict['age']
	print 'My country of birth is', person_dict['country']
	print 'My favorite language is', person_dict['language']

makeAndReadDict(['name','age','country','language'], ['Kaan', 22, 'Turkey', 'Python'])