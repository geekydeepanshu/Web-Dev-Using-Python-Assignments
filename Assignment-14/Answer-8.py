l=[4,5,7,4.5,4,5,4,7.5,7,4.5]
list=[]
for e in l:
    if e not in list:
        list.append(e)
for e in list:
    print(e,l.count(e),sep="  ") 