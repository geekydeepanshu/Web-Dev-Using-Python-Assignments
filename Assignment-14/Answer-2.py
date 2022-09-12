n=int(input("Enter a natural number: "))
odd_natural_number=[]
for x in range(1,2*n):
    if x%2!=0:
        odd_natural_number.append(x)
print(odd_natural_number)        
