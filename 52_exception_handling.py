#accept user's age and calculate remaining year in job. if age is above 60 or less then 18, raise custom exception 
try:
    age = int(input("Enter age (between 18 to 60)"))
    if age<18 or age>60:
        raise ValueError("age must be in range of 18 to 60")
    difference = 60 - age 
    print(f"year remaining for service = {difference}")
except ValueError as e:
    print(f"invalid age error is {e}")