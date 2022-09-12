a=-1
b=1
n=int(input("Enter number of terms to be print: "))
for x in range(1,n+1):
    c=a+b
    print(c,end=" ")
    a=b
    b=c