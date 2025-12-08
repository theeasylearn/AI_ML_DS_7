#write a program to accept product purchrase & sales price and findout profit or loss or break even amount (use if elif decision)
purchase_price = int(input("Enter product purchase price"))
sales_price = int(input("Enter product sales price"))

difference = sales_price - purchase_price

if difference>0:
    print(f"you have made profit of {difference} rs")
elif difference<0:
    print(f"you have made loss of {difference} rs")
else:
    print(f"you are on break even (no profit no loss)")
print("Good bye")