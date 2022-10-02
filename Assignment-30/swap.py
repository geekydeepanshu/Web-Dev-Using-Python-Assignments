def number_input():
    try:
        first_number=int(input("Enter First Numbers: "))
        second_number=int(input("Enter Second Numbers: "))
        return (first_number,second_number)
    except Exception:
        print("\nEnter Numbers Only !\n")
        return number_input()    


first_number,second_number=number_input()
first_number,second_number=second_number,first_number
print("After Swapping........\nFirst Number is {} and Second Number is {}".format(first_number,second_number))


