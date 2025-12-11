# write a program to findout compound interest of given amount, rate, year 
amount = int(input("Enter amount")) #1000
rate = int(input("Enter rate")) # 12
year = int(input("Enter year")) #5

original_amount = amount
count = 1
while count<=year:
    interest = (amount * rate * 1) / 100
    amount = amount + interest
    count+=1
interest = amount - original_amount
print(f"Compound Interest = {interest}")



