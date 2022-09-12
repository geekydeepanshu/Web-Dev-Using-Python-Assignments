sum=0
binary="0b"
n=int(input("Enter a number: "))
for x in range(31,-1,-1):
    if n>=2**x and (sum + 2**x)<=n:
        sum+=2**x
        binary+=str(1)
    else:
        if sum!=0:
            binary+=str(0)    
print(binary)            