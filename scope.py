X = 25
def my_func():
     X = 50
     return X

#______________
print(X)
# Will print X = 25 

#______________
print(my_func())
#Will print X = 50

#______________
my_func()
print(X)
#Will print x = 25


#Enclosing function locals
name = "this is global"

def greet():
    name = "Sammy"
    def hello():
        print("Hello"+name)
    hello()
greet()
#_________________________
# if i don't call hello() in the end of the greet() function, nothing will happen
