# write a program to print below series
# 1 8 27  64 125 ..... 10000
# 1 2 3   4  5
num = 1

while num<=21:
    qube = num * num * num  #1
    print(qube,end=' ')
    num = num + 1 #2 
print() #new line
print("Good bye")