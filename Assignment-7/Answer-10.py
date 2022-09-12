string=input("Enter your favourate colour: ")
split_string=string.split()
colour=split_string[2]
match colour:
    case "yellow":
        print("Monday")
    case "blue":
        print("Tuesday")        
    case "orange":
        print("Wednesday")  
    case "white":
        print("Thrusday")
    case "black":
        print("Friday")
    case "red":
        print("Saturday")
    case _:
        print("Sunday")                                      