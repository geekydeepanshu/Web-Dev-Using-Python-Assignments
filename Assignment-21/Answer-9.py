def numberMultiple(number,n):
    if n>0:
        numberMultiple(number,n-1)
        print(number*n,end=" ")

numberMultiple(int(input("Enter Number: ")),int(input("Enter a Number of multiple to be print: ")))