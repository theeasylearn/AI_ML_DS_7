# write a program to findout whether given year is leap year or not
year = int(input("Enter year"))
reminder1 = year % 4
reminder2 = year % 100
reminder3 = year % 400
if reminder1 == 0 and reminder2 !=0: #outer decision 
    print(f"{year} is leap year")
else: 
    if reminder2 == 0 and reminder3==0: #inner decision making
        print(f"{year} is leap year")
    else:
        print(f"{year} is not leap year")
