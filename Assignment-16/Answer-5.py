t=tuple([eval(e) for e in input("Enter elements of tuple: ").split(",")])
i=0
while i<len(t)-1:
    if t[i]!=t[i+1]:
        print("All the elements in given tuple are not same ")
        break
    i+=1
else:
    print("All the elements in given tuple are same")    