def draw_stars(x):
	for i in range(0,len(x)):
		for j in range(0,x[i]):
			print '*',
		print '\n'

draw_stars([4, 6, 1, 3, 5, 7, 25])

def draw_stars1(x):
	for i in range(0,len(x)):
		if isinstance(x[i], str) :
			for j in range(0,len(x[i])):
				print (x[i][0]).lower(),
			print '\n'
		elif isinstance(x[i], int):
			for j in range(0,x[i]):
				print '*',
			print '\n'

draw_stars1([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])