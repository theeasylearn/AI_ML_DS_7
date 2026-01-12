#import module mymath (must be in same folder)
import mymath
number = int(input("Enter number"))
square = mymath.getSquare(number)
print(square)

qube = mymath.getQube(number)
print(qube)
