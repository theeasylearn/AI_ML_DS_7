#print multiplication table of given number 
'''
    number = 5 
    5 x 1 = 5
    5 x 2 = 10
    5 x 3 = 15
    ..........
    5 x 10 = 50
'''
number = int(input("Enter number")) #5 
    
for multiplier in range(1,11):
    answer = number * multiplier #5
    print(f"{number} x {multiplier:2} = {answer:3}")

