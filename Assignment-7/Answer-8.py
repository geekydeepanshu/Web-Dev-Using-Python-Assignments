a=input("Enter two Strings: ")
b=input()
match 1 if a==b else (0 if b>a else -1):
    case 1:
        print("Given strings are identical")
    case 0:
        print("First string comes before the second in dictionary order")
    case -1:
        print("First string comes after the second string in dictionary order")