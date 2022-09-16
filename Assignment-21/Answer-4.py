# Write a recursive python function to print first N odd natural numbers in reverse order

def recursive_OddNaturalReverse(n):
    if n>0:
        a=2*n-1
        if a%2!=0:
            print(a,end=" ")
        recursive_OddNaturalReverse(n-1)

recursive_OddNaturalReverse(int(input("Enter a Number:  ")))