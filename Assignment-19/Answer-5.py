def func(t=[]):
    print("Given Elements are :",end=" ")
    for e in t:
        print(e,end=" ")

n=int(input("Enter Number of arguments for function: "))
list=[]
for x in range(n):
    list.append(eval(input("Enter Arguments for function: ")))
func(list)