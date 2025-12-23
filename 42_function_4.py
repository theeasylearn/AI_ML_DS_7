def getCalculation(num1,num2):
    addition = num1 + num2 
    subtraction = num1 - num2 
    multiplication = num1 * num2 
    division = num1 / num2 
    return addition,subtraction,multiplication,division #return multiple value 

num1 = int(input("Enter 1st number"))
num2 = int(input("Enter 2nd number"))

result = getCalculation(num1,num2)
print('all operations')
print(result)
print("addition = ",result[0])
print("subtraction = ",result[1])
print("multiplication = ",result[2])
print("division = ",result[3])