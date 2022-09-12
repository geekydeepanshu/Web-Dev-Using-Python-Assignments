def FibonacciGenerator(n):
    a,b=0,1
    while n:
        yield a
        a,b=b,a+b
        n-=1
for e in FibonacciGenerator(int(input("Enter a Required number of digits of fibonacci series: "))):
    print(e,end=" ")
