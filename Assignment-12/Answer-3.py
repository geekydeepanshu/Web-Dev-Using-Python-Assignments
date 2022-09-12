for n in range(1,101):
    i=0
    for a in range(1,n+1):
        if n%a==0:
            i+=1
    if i==2:
        print(n,end=" ")  