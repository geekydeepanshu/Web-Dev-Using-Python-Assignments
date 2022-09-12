def oddNatural(n):
    if n==1:
        return 1
    odd= 2 + oddNatural(n-1)
    return odd

print(oddNatural(int(input("Enter a Natural Number: "))))