year=int(input("Enter a Year: "))
match (2 if year%400==0 else 4)if year%100==0 else (1 if year%4==0 else 3):
    case 1:
        print("Non century leap year")
    case 2:
        print("Century leap year")    
    case 3:
        print("Non century non leap year") 
    case 4:
        print("Century non leap year")       