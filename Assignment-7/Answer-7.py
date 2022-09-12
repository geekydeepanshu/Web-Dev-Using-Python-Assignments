number=int(input("Enter a Number: "))
match (1 if number>0 else 0) if number>=0 else -1:
    case 1:
        print("Positive")
    case -1:
        print("Negative")  
    case 0:
        print("Zero")      