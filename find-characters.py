l = ['hello','world','my','name','is','Anna']
char = 'n'
output = []

for i in range(0,len(l)):
	for j in range(0, len(l[i])):
		if (l[i][j] == char):
			output.append(l[i])
			break
print output