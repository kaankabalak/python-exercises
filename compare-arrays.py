list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','milk']

isEqual = True
if len(list_one) == len(list_two):
	for i in range(0,len(list_one)):
		if list_one[i] == list_two[i]:
			pass
		else:
			isEqual = False
else:
	isEqual = False
if isEqual:
	print 'The lists are the same'
else:
	print 'The lists are not the same'