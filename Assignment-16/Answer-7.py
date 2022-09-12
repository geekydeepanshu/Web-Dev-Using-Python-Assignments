tuple_1=(1,2,3,4,5,6)
l=[]
for e in tuple_1:
    if e==4 or e==5:
        l.append(e)
tuple_2=tuple(l)   
print(tuple_2)     