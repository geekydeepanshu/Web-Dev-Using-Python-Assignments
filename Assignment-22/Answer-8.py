def naturalCubes(n):
    if n==1:
        return 1
    return n**3 + naturalCubes(n-1)

print(naturalCubes(int(input("Enter a Natural Number: "))))