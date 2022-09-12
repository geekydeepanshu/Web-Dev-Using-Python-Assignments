def numberInRange(beg,end,step,number):
    ( print("Yes") if number in range(beg,end,step) else print("No"))


beg=int(input("Enter Begning value of Range(Inclusive): "))
end=int(input("Enter End value of Range(Exclusive): "))
step=int(input("Enter Step value of Range: "))
number=int(input("Enter Number: "))
numberInRange(beg, end, step, number)