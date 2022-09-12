number=input("Enter a three digit number: ")
if(len(number)==3):
    number=int(number)//10
    number%=10
    print("Second digit of given three digit number is: ",number)
else:
    print("Given number is not a three digit number")  