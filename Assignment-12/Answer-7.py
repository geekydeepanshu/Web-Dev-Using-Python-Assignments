a=int(input("Enter two numbers: "))
b=int(input())
c=a if a>b else b
count=0
for x in range(1,c+1):
    if a%x==0 and b%x==0:
        count+=1
if count==1:
    print("Given numbers are pair of co-prime numbers")  
else:          
    print("Given numbers are not pair of co-prime numbers")