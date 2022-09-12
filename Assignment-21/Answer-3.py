def oddNatural(n):
    if n==1:
        print(1,end=" ")
        return 1
    odd= 2 + oddNatural(n-1)
    print(odd,end=" ")
    return odd

oddNatural(int(input("Enter a Natural Number: ")))