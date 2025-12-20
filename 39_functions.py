#write a function for => (x+y)**2=x**2+2*x*y+y**2 using default argument

def square(x,y=4):
    res=x**2+2*x*y+y**2
    print(res)  
    
square(3)  

#switch argument
def animal(b,a):
    print(a)
    print(b)
    
a='cat'
b='dog'
animal(a,b)