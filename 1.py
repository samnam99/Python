#Example 1: 
print ("-------------------------------------------------------------------")
friends = ['john', 'pat', 'gary', 'michael']
for i, name in enumerate(friends):
    print ("iteration {iteration} is {name}".format(iteration=i, name=name))

#Example 2: 
print ("-------------------------------------------------------------------")
def greet(name):
	print ('Hello', name)
greet('Jack')
greet('Jill')
greet('Bob')

#Example 3: 
print ("-------------------------------------------------------------------")
def addnum(a, b):
	c=a+b
	print (c)

addnum(2,4)
addnum(5,6)


