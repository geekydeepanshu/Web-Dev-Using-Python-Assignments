tuple1 = (11, [22, 33], 44, 55)
tuple1=list(tuple1)
tuple1[1][0]=222
print(tuple(tuple1))