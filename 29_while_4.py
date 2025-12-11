#write a program to findout factorial of given number
#number = 5 process 5 x 4 x 3 x 2 x 1 = output 120
#number = 6 process 6 x 5 x 4 x 3 x 2 x 1 = output 720
number = int(input("Enter number")) #5
result = 1

while number>0:
    result = result * number #5
    number -= 1 #4
print(result)
