def coinToss():
	import math
	import random
	heads = 0
	tails = 0
	print 'Starting the program...'
	for i in range(1,5001):
		random_num = round(random.random())
		if random_num == 0:
			heads += 1
			print "Attempt #" + str(i) + ": Throwing a coin... It's a head! ... Got " + str(heads) + " head(s) so far and " + str(tails) + " tail(s) so far"
		elif random_num == 1:
			tails += 1
			print "Attempt #" + str(i) + ": Throwing a coin... It's a tail! ... Got " + str(heads) + " head(s) so far and " + str(tails) + " tail(s) so far"

coinToss()