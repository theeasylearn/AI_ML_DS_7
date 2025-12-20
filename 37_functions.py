# Without return value without argument
import shutil
import datetime 
def printLine():
    print("_"*100)
# Without return value  with argument 
def printInCenter(message):
    screen_width = shutil.get_terminal_size().columns
    print(message.center(screen_width))
# With return value without argument
def getDate():
    #local variable 
    #create datetime class object
    date = datetime.datetime.today() 
    today = str(date.day) + "-" + str(date.month) + "-" + str(date.year)
    return today

# With return value with argument 
def getSquare(number):
    #local variable
    square = number * number
    return square

printLine()
printInCenter("THE EASYLEARN ACADEMY")
printLine()
today = getDate()
print(today)

number = int(input("Enter number"))

result = getSquare(number)
print(f"suuare is {result}")