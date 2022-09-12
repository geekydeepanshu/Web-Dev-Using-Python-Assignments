def numberReverse(n):
    if n%10!=0:
        print(n%10,end="")
        numberReverse(n//10)

numberReverse(int(input("Enter a Natural Number: ")))