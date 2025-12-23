# write a program to convert decimal number into binary number 
number = 20
def toBinary(number):
    if number>0:
        reminder = number % 2 #0
        number = number // 2 #5
        toBinary(number) #recursion 5
        print(reminder,end='')

toBinary(number)
