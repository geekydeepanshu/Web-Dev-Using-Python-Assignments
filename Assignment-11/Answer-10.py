n=int(input("Enter a Number: "))
sum=0
octal="0o"
for a in range(9,-1,-1):
    if n>=8**a:
        count=0
        while sum+8**a<=n:
            sum+=8**a
            count+=1
        octal+=str(count) 
print("Given number has octal representation: ",octal)           