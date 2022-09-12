sum=0
n=input("Enter a Number: ")
for x in n:
    if ord(x)>=48 and ord(x)<=57:
        sum+=int(x)
print("sum of digits of given number is: ",sum)  