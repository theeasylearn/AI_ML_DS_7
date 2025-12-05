# write a program to findout profit/loss amount and display it. accept purchase and sale price from user to decide profit/loss 
purchase_price = int(input("enter product purchase price"))
sale_price = int(input("Enter Sales price"))
difference = sale_price - purchase_price 

if difference>0:
    print(f"you have made profit of {difference}")

if difference<0:
    print(f"you have made loss of ",difference)

if difference==0:
    print("you have made no profit no loss")

print("Thank you")

