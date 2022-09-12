string=input("Enter a String: ")
match len(string):
    case 0:
        print("Empty String")
    case 1:
        print("Single word string")
    case _:
        print("Multi word String")    