#write a program to make sum of all values & find average of all elements list
numbers = [10,20,None,30,40,'Ankit',50]
# numbers = [None,False,'Ankit',True]
sum = 0 
count = 0
for item in numbers:
    print(item) 
    try:
        if item !=True and item !=False:
            sum=sum + item #if this line has error, next line will not execute 
            count = count + 1
    except TypeError:
        print(f"{item} is not valid number, so it is skipped")
try:
    mean = sum / count
    print(f"sum = {sum} mean = {mean}")
except ZeroDivisionError:
    print("none of the value is valid hence sum and means is not required")