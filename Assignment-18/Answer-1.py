my_information = {}
n=int(input("How Many Information Do You Want To Store: "))
for e in range(n):
    key=input("Enter Detail Heading: ")
    data=eval(input("Enter Detail: "))
    my_information[key]=data
print(my_information)
