number=complex(input("Enter a complex number: "))
real_part=number.real
imaginary_part=number.imag
if real_part>imaginary_part:
    print("Greater is: ",real_part)
else:
    print("Greater is: ",imaginary_part)    
