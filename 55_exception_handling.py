#write a program to accept RTO Driving Licence test book date from user as per business rule. 
# date must be in range of tomorrow to 60 days from today. program not stop until user books 
from datetime import datetime as dt, timedelta as td  
class InvalidBookingDate(Exception):
    pass 
#store tomorrow date 
tomorrow = dt.now() + td(days=1)
max_booking_date = dt.now() + td(days=60)
print(tomorrow)
print(max_booking_date)
while True:
    try:
        #accept booking date from user 
        book_date = input(f"Enter booking(dd-mm-YYYY) date must be between {tomorrow} to {max_booking_date}")
        print(book_date)
        #convert string date into date 
        book_date = dt.strptime(book_date,"%d-%m-%Y")
        print(book_date)
        if book_date<tomorrow or book_date>max_booking_date:
            raise InvalidBookingDate()
        if book_date.day.weekday() == 6:
             raise InvalidBookingDate()
        break
        
    except ValueError as e:
        print("invalid date, date must be given in dd-mm-YYYY format")
    except InvalidBookingDate as e:
        print("booking date must be between {tomorrow} to {max_booking_date} and must not be sunday")