#exception handling mechanism in python 
try:
    num1 = int(input("Enter first number"))
    num2 = int(input("Enter 2nd number"))
    result = num1 / num2 
except ValueError:
    print("only numbers allowed as input")
except ZeroDivisionError:
    print("denominator must not be zero")
else:
    print("division = ",result)
finally:
    print("thank you for using our program")