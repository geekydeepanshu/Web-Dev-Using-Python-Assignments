n=input("Enter a Number: ")
i,reverse=0,0
for a in n:
    reverse+=(10**i)*int(a)
    i+=1
print("Number after reverseing its digits is : ",reverse)    