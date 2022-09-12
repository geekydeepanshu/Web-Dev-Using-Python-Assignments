n=int(input("Enter a natural number: "))
even_natural_number=[]
for x in range(2*n-1):
    if x%2==0:
        even_natural_number.append(x)
print(even_natural_number)