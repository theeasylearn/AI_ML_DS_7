#pythagoras equation

#a^2+b^2=c^2

#Without return value without argument
def pythagoras():
    a=int(input("Enter the number"))
    b=int(input("Enter the number"))
    
    c=(a**2+b**2)**0.5
    print(c)
    
pythagoras()

#Without return value with argument
def pythagoras(a,b):
    
    c=(a**2+b**2)**0.5
    print(c)

a=int(input("Enter the number"))
b=int(input("Enter the number"))
pythagoras(a,b)

#With return value without argument
def pythagoras():
    a=int(input("Enter the number"))
    b=int(input("Enter the number"))
    c=(a**2+b**2)**0.5
    return c

result=pythagoras()
print(result)

#With return value with argument
def pythagoras(a,b):
    
    c=(a**2+b**2)**0.5
    return c

a=int(input("Enter the number"))
b=int(input("Enter the number"))
result=pythagoras(a,b)
print(result)