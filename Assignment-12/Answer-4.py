a=int(input("Enter Two Numbers: "))
b=int(input())
for n in range(a,b+1):
    i=0
    for a in range(1,n+1):
        if n%a==0:
            i+=1
    if i==2:
        print(n,end=" ") 