n=int(input("Enter a number: "))
c,x=0,1
while c!=n:
    i=0
    for a in range(1,x+1):
        if x%a==0:
            i+=1
    if i==2:
        print(x,end=" ")
        c+=1
    x+=1        