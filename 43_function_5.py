#example of lambda function 
getSquare = lambda num1: num1 * num1 
getInterest = lambda amount,rate,year: (amount * rate * year) / 100

num1 = int(input("Enter number 1"))

amount = float(input("Enter amount: "))
rate = float(input("Enter rate: "))
year = int(input("Enter year: "))

interest = getInterest(amount,rate,year)
print("Simple interest is ",interest)
print("Square of given number",getSquare(num1))
