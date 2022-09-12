n=int(input("Enter a number: "))
i=0
for a in range(1,n+1):
    if n%a==0:
        i+=1
if i==2:
    print("Prime Number")
else:
    print("Not Prime Number")            
