list1=[1,2,3,4,5,6]
list2=[11,22,33,44,55,66]
d={list1[i]:list2[i] for i in range(len(list1))}
print(d)