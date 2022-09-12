from re import I


def oddNaturalGenerator(n):
    i=0
    while n:
        if i%2!=0:
            yield i
            n-=1
        i+=1
for e in oddNaturalGenerator(int(input("Enter a Natural Number: "))):
    print(e,end=" ")