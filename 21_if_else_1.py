# #Write a program that takes a 5 subject marks from student. findout whether student is passed or failed if user has above 39 marks in each and every subject, he is passed otherwise failed.
marks = [0,0,0,0,0]
marks[0] = int(input("Enter 1st subject marks"))
marks[1] = int(input("Enter 2nd subject marks"))
marks[2] = int(input("Enter 3rd subject marks"))
marks[3] = int(input("Enter 4th subject marks"))
marks[4] = int(input("Enter 5th subject marks"))

if marks[0]>38 and marks[1]>38 and marks[2]>38 and marks[3]>38 and marks[4]>38: 
    print("you are passed")
else:
    print("you are failed")

print("Good bye...")