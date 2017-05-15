# Multiples
# Part 1
for i in range(1,1000):
	if i % 2 != 0:
		print i
# Part 2
count = 5
while count <= 1000000:
	print count
	count += 5
# Sum List and Average List
a = [1,2,5,10,255,3]
sum = 0
for element in a:
	sum += element
print 'The sum of the elements in the list is:', sum
# Average list starts here
avg = float(sum)/len(a)
print 'The average of the elements in the list is:', avg