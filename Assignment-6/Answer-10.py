a=int(input("Enter three numbers: "))
b=int(input())
c=int(input())
if a==b==c:
    print("Greatest number among given numbers is : ",a)
else:
    if a>b:
        if a>c:
            print("Greatest number among given numbers is : ",a)
        else:
            print("Greatest number among given numbers is : ",c)     
    else:
        if b>c:
            print("Greatest number among given numbers is : ",b)
        else:
            print("Greatest number among given numbers is : ",c)               