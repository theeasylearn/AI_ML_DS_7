#write a program to accept friend name from user and store it into file.
filename = 'friends.txt'
mode = 'w'
with open(filename,mode) as file:
    name = input("What is your friend name")
    mobile = input("What is his/her contact no")
    content = f"name = {name} mobile = {mobile} \n"
    file.append(content)
file.close()
print("data saved successfully")
