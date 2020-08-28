def addNum(num1,num2):
    if type(num1) == type(num2)==type(10):
        return num1+num2
    else:
        return "sorry, i need an integer"
result = addNum('2','3')
print (result)