l = [3.14, 2.5, 5.8, 4.4]
sum = 0
string = ''
isInt = False
isFloat = False
isStr = False
for element in l:
	if isinstance(element, int):
		isInt = True
		sum += element
	elif isinstance(element, float):
		isFloat = True
		sum += element
	elif isinstance(element, str):
		isStr = True
		string = string + ' ' + element

if (isInt == True and isFloat == True) or (isInt == True and isStr == True) or (isFloat == True and isStr == True):
	print 'The array you entered is of mixed type'
elif isInt == True:
	print 'The array you entered is of integer type'
elif isStr == True:
	print 'The array you entered is of string type'
elif isFloat == True:
	print 'The array you entered is of float type'

if isStr == True:
	string = string[1:]
	print 'String:', string

if isInt or isFloat:
	print 'Sum:', sum