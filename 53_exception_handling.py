#accept user's age and calculate remaining year in job. if age is above 60 or less then 18, raise custom exception. program must not stop until it complete task  (calculate remaining year in job)
while True: #it is infinite loop but it must stop after calculation and display of remaining year in job
    try:
        age = int(input("Enter age (between 18 to 60)"))
        if age<18 or age>60:
            raise ValueError("age must be in range of 18 to 60")
        difference = 60 - age 
        print(f"year remaining for service = {difference}")
        break #break loop 
    except ValueError as e:
        error_msg = str(e) 
        if "invalid literal for int()" in error_msg.lower():
            print("age is string, it must be numbers")
        else:
            print(f"invalid age, age must between 18 to 60")

print("good bye....")