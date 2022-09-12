sum=0
n=int(input("Enter a Natural Number: "))
for x in range(1,n+1):
    sum+=x**3
print("Sum of Square of First %d natural numbers is %d"%(n,sum))  