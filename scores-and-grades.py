import random
import math
grade = 'D'
for i in xrange(0,10):
	random_num = int(math.floor(41*random.random() + 60))
	if random_num < 70 and random_num >= 60:
		grade = 'D'
	elif random_num < 80:
		grade = 'C'
	elif random_num < 90:
		grade = 'B'
	elif random_num <=100:
		grade = 'A'
	print 'Score: ' + str(random_num) + '; Your grade is ' + grade