# write a program to print following pattern 
'''
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
'''
for row in range(6,0,-1):
    for astrik in range(1,row):
        print(astrik,end=' ')
    print()


