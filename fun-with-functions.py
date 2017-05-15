# Odd/Even
def oddEven():
	for i in range(1,2001):
		if i % 2 == 0:
			print 'Number is ' + str(i) + '. This is an even number.'
		else:
			print 'Number is ' + str(i) + '. This is an odd number.'

oddEven()

# Multiply
def multiply(a, num):
	for i in range(0,len(a)):
		a[i] *= num
	return a

print multiply([2,4,10,16], 5)

# Layered multiples
def layered_multiples(arr):
	new_array = []
	for i in range(0,len(arr)):
		new_array.append([])
		for j in range(0,arr[i]):
			new_array[i].append(1)
	return new_array

print layered_multiples(multiply([2,4,5], 3))