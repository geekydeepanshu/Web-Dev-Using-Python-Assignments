# Write a recursive python function to print first N even natural numbers in reverse order.

def recursive_EvenNaturalReverse(n):
    if n>0:
        a=2*n
        if a%2==0:
            print(a,end=" ")
        recursive_EvenNaturalReverse(n-1)

recursive_EvenNaturalReverse(int(input("Enter a Number:  ")))