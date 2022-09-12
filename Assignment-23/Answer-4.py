def squareNaturalGenerator(n):
    i=1
    while i<=n:
        yield (i**2)
        i+=1
for e in squareNaturalGenerator(int(input("Enter a Natural Number: "))):
    print(e,end=" ")
