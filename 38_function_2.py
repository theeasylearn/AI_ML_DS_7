#Arbitrary Argument functions
def getTotal(*numbers):
    total = 0 #local variable
    for num in numbers:
        total = total + num
    return total 

result = getTotal(10,20,30,100,200,500)
print(f"total = {result}")

result = getTotal(5000,2500,1000,150)
print(f"total = {result}")
