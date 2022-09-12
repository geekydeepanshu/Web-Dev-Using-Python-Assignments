def naturalNumber(n):
    if n>0:
        naturalNumber(n-1)
        print(n,end=" ")

naturalNumber(int(input("Enter a Natural Number: ")))