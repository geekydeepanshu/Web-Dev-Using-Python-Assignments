import functools

def sumList(a,b):
    return a+b

list=[]
for x in range(int(input("Enter Number of elements in List: "))):
    list.append(int(input()))

sum=functools.reduce(sumList,list)
print(sum)