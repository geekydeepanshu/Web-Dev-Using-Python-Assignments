year=int(input("Enter a year: "))
if year%100==0:
    if year%400==0:
        print("Leap Year")
    else:
        print("Not a Leap Year") 
else:
    if year%4==0:
        print("Leap Year")
    else:
        print("Not a Leap Year")               