sum=0
n=int(input("Enter a Natural Number: "))
for x in range(1,2*n):
    if x%2!=0:
        sum+=x
print("Sum of first %d odd natural numbers is %d"%(n,sum))        