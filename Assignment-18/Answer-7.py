d1,d2,d3={},{},{}
n=int(input("Enter Number of Elements In Dictionary 1 :"))
for x in range(n):
    key=input("Enter Key Value: ")
    data=input("Enter Data Value: ")
    d1[key]=data
n=int(input("Enter Number of Elements In Dictionary 2 :"))
for x in range(n):
    key=input("Enter Key Value: ")
    data=input("Enter Data Value: ")
    d2[key]=data
n=int(input("Enter Number of Elements In Dictionary 3 :"))
for x in range(n):
    key=input("Enter Key Value: ")
    data=input("Enter Data Value: ")
    d3[key]=data
d_main={1:d1,2:d2,3:d3}
print(d_main)