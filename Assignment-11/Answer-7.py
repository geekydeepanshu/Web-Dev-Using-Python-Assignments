count=0
n=input("Enter a Number: ")
for x in n:
    if ord(x)>=48 and ord(x)<=57:
        count+=1
print("Number of digits in given number are: ",count)    