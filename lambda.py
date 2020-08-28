#Lambda Expression

#Filter
mylist = [1,2,3,4,5,6,7,8]

#def even_bool(num):
#    return num%2==0

#evens = filter(even_bool,mylist)
#print(list(evens))

#we can replace this with a simpler syntax
evens= filter(lambda num:num%2 == 0,mylist)
print(list(evens))