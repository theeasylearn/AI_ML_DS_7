#without argument

#with return 

def square():
    num=int(input("Enter the number: "))
    square=num*num
    return square

result=square()
print(result)

#without return
# def square():
#     num=int(input("Enter the number: "))
#     square=num*num
#     print(square)

# square()


#with argument

def square(num):
    square=num*num
    return square

num=int(input("Enter the number: "))
result=square(num)
print(result)
