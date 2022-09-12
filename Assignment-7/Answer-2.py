a=int(input("Enter two numbers: "))
b=int(input())
print(" ")
print("Select a Operation: \n","1.Addition","2.Substraction","3.Multiplication","4.Division",sep="\n")
choice=int(input("Enter your choice: "))
match choice:
    case 1:
        print("Result after Adding a and b is: ",a+b)
    case 2:
        print("Result after Substracting a and b is: ",a-b)
    case 3:
        print("Result after Multiplying a and b is: ",a*b)
    case 4:
        print("Result after Dividing a and b is: ",a/b)         
    case _:
        print("Invalid Choice Selected ")    