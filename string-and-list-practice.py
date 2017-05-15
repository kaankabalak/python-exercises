# Find and Replace
print 'Find and Replace:'
str = "It's thanksgiving day. It's my birthday, too!"
idx = str.find('day')
print idx
print str.replace('day','month',1)
# Min and Max
print 'Min and Max:'
x = [2,54,-2,7,12,98]
print x
print min(x)
print max(x)
# First and Last
print 'First and Last:'
x = ["hello",2,54,-2,7,12,98,"world"]
print x
print x[0]
print x[len(x)-1]
# New List
print 'New List:'
x = [19,2,54,-2,7,12,98,32,10,-3,6]
print x
x.sort()
print 'Sorted list:', x
y = x[:len(x)/2]
print 'Bottom half of list:', y
x = x[len(x)/2:]
print 'Other half of list:', x
x.insert(0,y)
print 'Final output:', x