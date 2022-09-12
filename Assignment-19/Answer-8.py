import functools

def multiplyList(a,b):
    return a*b

list=[]
for x in range(int(input("Enter Number of elements in List: "))):
    list.append(int(input()))
print(functools.reduce(multiplyList,list))