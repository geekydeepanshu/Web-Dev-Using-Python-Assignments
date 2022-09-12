s={1,2,3,4,5,6}
a=iter(s)
i=0
while i<len(s):
    print(next(a),end=" ")
    i+=1