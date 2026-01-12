#develop as module 
#create function
#with argument with return value
def getSquare(number):
    #create local variable
    square = number * number 
    return square 

#with argument with return value
def getQube(number):
    square = getSquare(number)
    qube = square * number
    return qube


