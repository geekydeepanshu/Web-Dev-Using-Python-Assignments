def naturalReverse(n):
    if n>0:
        print(n,end=' ')
        naturalReverse(n-1)



naturalReverse(int(input("Enter a Natural Number: ")))