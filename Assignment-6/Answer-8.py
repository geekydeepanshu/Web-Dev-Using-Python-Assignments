a=int(input("Enter cofficent of x^2 term : "))
b=int(input("Enter cofficent of x term : "))
c=int(input("Enter cofficent of contant term : "))
d=(b**2)-(4*a*c)
if(d>0):
    print("Two distinct and real roots")
elif (d==0):
    print("Two equal and real roots")
else:
    print("Two distinct and imaginary roots")        