tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))
tuple2,tuple3=[],[]
i=0
for e in tuple1:
    tuple2.append(tuple1[i][::-1])
    i+=1
tuple1=sorted(tuple2)
i=0
for e in tuple1:
    tuple3.append(tuple1[i][::-1])
    i+=1
print(tuple(tuple3))    