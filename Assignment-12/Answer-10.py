a=int(input("Enter two numbers: "))
b=int(input())
c=a if a>b else b
for x in range(1,c+1):
    if a%x==0 and b%x==0:
        h=x
print("HCF of given numbers are: ",h)        