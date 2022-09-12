factorial=1
n=int(input("Enter a Number: "))
for x in range(n,0,-1):
    factorial*=x
print("Factorial of Given Number is ",factorial)    