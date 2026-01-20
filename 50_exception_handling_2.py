#concept of exceptional handling 
#exception handling mechanism in python 
try:
    num1 = int(input("Enter first number"))
    num2 = int(input("Enter 2nd number"))
    result = num1 / num2 
    print("division = ",result)
except (ValueError, ZeroDivisionError):
    print("only numbers allowed as input and it must be non zero")
