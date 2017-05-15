for k in range (0,13):
	if k == 0:
		print 'x',
	else:
		print k,

print '\n'
for i in range(1,13):
	for j in range (1,13):
		if j == 1:
			print i,
			print i*j,
		else:
			print i*j,
	print '\n'