n=int(input("Enter a Numbers: "))
prime,b=True,1
while prime:
    i=0
    for a in range(1,n+b+1):
        if (n+b)%a==0:
            i+=1   
    if i==2:
        print("Prime Number after given number is ",(n+b))
        prime=False   
    b+=1