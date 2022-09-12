def evenNaturalGenerator(n):
    i=1
    while n:
        if i%2==0:
            yield i
            n-=1
        i+=1
for e in evenNaturalGenerator(int(input("Enter a Natural Number: "))):
    print(e,end=" ")
