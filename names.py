# Part 1
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def names(students):
	for i in range(0,len(students)):
		print students[i]['first_name'], students[i]['last_name']

names(students)

# Part 2
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def names2(users):
 	print 'Students'
 	for i in range(0,len(users['Students'])):
 		print (i+1) , '-', users['Students'][i]['first_name'].upper(), users['Students'][i]['last_name'].upper(), '-' , str(len(users['Students'][i]['first_name']) + len(users['Students'][i]['last_name']))
	print 'Instructors'
 	for i in range(0,len(users['Instructors'])):
 		print (i+1) , '-', users['Instructors'][i]['first_name'].upper(), users['Instructors'][i]['last_name'].upper(), '-' , str(len(users['Instructors'][i]['first_name']) + len(users['Instructors'][i]['last_name']))

names2(users)