'''
write a program to findout minimum marks & subject name and maximum marks and subject name from given dictionary 
'''
marks = {"Math": 35, "English": 99, "Science": 25, "History": 80, "Geography": 78, "Computer": 100}
min = marks['Math'] # 88
max = marks['Math'] # 88
min_subject = "Math"
max_subject = "Math"
for subject in marks:
    # print(subject)
    # print(marks[subject])
    if marks[subject]<min:
        min = marks[subject]
        min_subject = subject
    if marks[subject]>max:
        max = marks[subject]
        max_subject = subject
print(f"minimum marks = {min} maximum marks = {max}")
print(f"minimum subject name = {min_subject} maximum subject name = {max_subject}")