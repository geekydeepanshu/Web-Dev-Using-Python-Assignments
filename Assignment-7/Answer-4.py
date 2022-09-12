age=int(input("Enter Age: "))
if age>0 and age<100:
    if age>0 and age<10:
        print("Kid")
    elif age>=10 and age<20:
        print("Teen")
    elif age>=20 and age<40:
        print("Young")
    elif age>=40 and age<60:
        print("Experienced")
    else:
        print("Senior Citizen")       
else:
    print("Warning ! Invalid age Entered")    