def checkPrime(n):
    c=0
    for x in range(1,n+1):
        if n%x==0:
            c+=1
    return True if c==2 else False


print("Prime Number" if checkPrime(int(input("Enter a Number: "))) else "Not a Prime Number")