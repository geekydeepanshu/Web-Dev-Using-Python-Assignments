def evenNatural(n):
    if n==1:
        print(2,end=" ")
        return 2
    even=2+ evenNatural(n-1)
    print(even,end=" ")
    return even



evenNatural(10)