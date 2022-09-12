a=int(input("Enter length of three sides of Tringle: "))
b=int(input())
c=int(input())
print(" ")
print("Select a Option: \n","1.Check whether a given set of three numbers are lengths of an isosceles triangle or not","2.Check whether a given set of three numbers are lengths of sides of a right angled triangle or not","3.Check whether a given set of three numbers are equilateral triangle or not","4.Exit",sep="\n")
choice=int(input("Enter Your Choice: "))
match choice:
    case 1:
        if a==b or b==c or a==c:
            print("Sides of a Isoceleus Tringle")
        else:
            print("Sides of a not Isoceleus Tringle")    
    case 2:
            if a>b:
                 if a>c:
                    x,y,z=c,b,a
                 else:
                     x,y,z=a,b,c     
            else:
                 if b>c:
                     x,y,z=c,a,b
                 else:
                    x,y,z=a,b,c     
            if (x**2) + (y**2) == (z**2):
                print("Sides of a Right Angled Tringle")
            else:
                print("Sides of a not Right Angled Tringle")    
    case 3: 
        if a==b==c:
            print("Sides of a Equilateral Tringle")   
        else:
            print("Sides of not a Equilateral Tringle")  
    case 4:
        pass
    case _:
        print("Invalid Choice ")                  