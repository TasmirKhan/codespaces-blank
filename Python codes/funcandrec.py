def average(a,b,c):
    print((a+b+c)/3)
    return (a+b+c)/3

def mult(a,b):
    print(a*b)
    return a*b

def factorial(a=1):
    i=1
    temp =1
    while i<=a:
        temp = temp*i
        i+=1
    print("Factorial of",a,"is",temp)


def currencychange(a=1):
    print(a,"dollar =",a*85.50)
    return a*85.50

def printlist(a):
    
a =20
b=40
c=5
list = [1,2,3,4]
average(a,b,c)
mult(a*b,c)
factorial(c)
currencychange()
printlist(list)