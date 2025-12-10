# write a program to print below series
# 0 1 1 2 3 5 8 13 21 ......... 100
prev = 0
curr = 1
print(prev,end=' ')
print(curr,end=' ')
next = prev + curr

while next<100:
    print(next,end=' ')
    prev = curr #
    curr = next # 1
    next = prev + curr

