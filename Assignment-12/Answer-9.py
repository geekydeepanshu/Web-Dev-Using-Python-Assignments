a=int(input("Enter two numbers: "))
b=int(input())
c=a if a>b else b
i=1
while True:
    if (c*i)%a==0 and (c*i)%b==0:
        print("LCM of given numbers is: ",c*i)
        break
    i+=1