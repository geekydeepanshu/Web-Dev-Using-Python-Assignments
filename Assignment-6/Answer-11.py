month=int(input("Enter month in numeric format: "))
if month>=1 and month<=12:
    if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12 :
        print("Number of days in given month are 31 days")
    elif month==2:
        print("Number of days in given month are 28 or 29(Leap Year) days")   
    else:
        print("Number of days in given month are 30 days")  
else:
    print("Warning ! You did not enter a valid month")           