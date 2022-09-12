list_original=[4,5,7,4.5,4,5,4,7.5,7,4.5]
list_distinct_elements=[]
for e in list_original:
    if e not in list_distinct_elements:
        list_distinct_elements.append(e)
for x in list_distinct_elements:
    print(x,end="   ")
    i=0
    for e in list_original:
        if x==e:
            print(i,end=" ")
        i+=1
    print("")        
