def fun2(a,b):
    return a+b

def fun1(list1=[]):
    a,b=tuple(list1)
    return fun2(a,b)
print(fun1([3,4]))