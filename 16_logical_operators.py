# example of relational operator
num1 = int(input("Enter 1st number")) #10
num2 = int(input("Enter 2nd number")) #20
num3 = int(input("Enter 3rd number")) #30

result = num1 < num2 and num2 < num3 # 10==20 and 20==30
print(f"{result} = {num1} < {num2} and {num2} < {num3}")

result = num1 < num2 or num2 < num3 # 10==20 and 20==30
print(f"{result} = {num1} < {num2} or {num2} < {num3}")

result = not (num1 < num2 and num2 < num3) # 10==20 and 20==30
print(f"{result} = not ({num1} < {num2} and {num2} < {num3})")

