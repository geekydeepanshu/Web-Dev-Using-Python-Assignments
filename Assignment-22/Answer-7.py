def naturalSquare(n):
    if n==1:
        return 1
    return n**2 + naturalSquare(n-1)

print(naturalSquare(int(input("Enter a Natural Number: "))))