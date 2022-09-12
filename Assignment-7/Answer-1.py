month=input("Enter a Month: ")
match month:
    case "January":
        print("January has 31 days")
    case "Feburary":
        print("Feburary has 28 or 29 (in leap year) days")
    case "March":
        print("March has 31 days")
    case "April":
        print("April has 30 days") 
    case "May":
        print("January has 31 days")
    case "June":
        print("June has 30 days")
    case "July":
        print("July has 31 days")
    case "August":
        print("August has 31 days") 
    case "September":
        print("September has 30 days")
    case "Octuber":
        print("Octuber has 31 days")
    case "November":
        print("November has 30 days")
    case "December":
        print("December has 31 days")
    case _:
        print("You did not enter a valid month")                                             
