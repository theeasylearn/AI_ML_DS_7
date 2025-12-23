#concept of keyword arguments
def getMerit(maths,science,english,computer,history,drawing):
    print(maths,science,english,computer,history,drawing)
    total = maths + science + english
    return	total

m = int(input("Enter Maths marks: "))
s = int(input("Enter Science marks: "))
e = int(input("Enter English marks: "))
c = int(input("Enter Computer marks: "))
h = int(input("Enter History marks: "))
d = int(input("Enter Drawing marks: "))

print(getMerit(d,h,c,e,s,m)) #bad way
print(getMerit(history=h,drawing=d,computer=c,maths=m,english=e,science=s)) #write way (keyword arguments)
