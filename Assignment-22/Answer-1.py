def naturalNumberSum(n):
    if n==1:
        return 1
    return n+ naturalNumberSum(n-1)

print(naturalNumberSum(int(input("Enter a Natural Number: "))))