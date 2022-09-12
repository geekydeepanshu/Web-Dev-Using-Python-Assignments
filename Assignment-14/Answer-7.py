list=eval(input("Enter a List: "))
list_int=[]
for x in list:
    if type(x)==int:
        list_int.append(x)
print(list_int)        