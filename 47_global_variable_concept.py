#example of global variable
balance = 2000
def addMoney(amount):
    global balance 
    balance = balance + amount 
    print("Balance inside add money =",balance)
def reduceMoney(amount):
    global balance 
    balance = balance - amount 
    print("Balance inside reduce money money =",balance)
print("balance before update ",balance)
addMoney(99) 
reduceMoney(1000)