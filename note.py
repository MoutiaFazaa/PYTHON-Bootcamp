#dictionnary
my_stuff =  {'lunch':'pizza' , 'breakfast':'eggs'}
my_stuff['lunch'] = 'burger'
my_stuff['dinner'] = 'pasta'

print(my_stuff['lunch'])
print(my_stuff)

#set : a list of unique elements
x = set()

x.add(1)
x.add(2)
x.add(3)
x.add(4)
x.add(4)
print(x)

converted = set([1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,4,4,4,5])
print(converted)