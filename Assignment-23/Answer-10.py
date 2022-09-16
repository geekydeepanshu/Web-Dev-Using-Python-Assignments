#Define a function which calculates HCF of two numbers. Define and apply a decorator to check whether two given numbers are co-prime or not.

def decorator_CoPrimeChecker(hcf):
    def CoPrimeCheck(a,b):
        if hcf(a,b)==1:
            print("Given Numbers Are Co-Prime")
        else:
            print("Hcf of {} and {} is {} ".format(a,b,hcf(a,b)))
    return CoPrimeCheck
@decorator_CoPrimeChecker
def hcf(frist_number,second_number):
    bigger_number = frist_number if frist_number>second_number else second_number
    while bigger_number :
       if frist_number%bigger_number==0 and second_number%bigger_number==0:
           return bigger_number
       bigger_number-=1

hcf(int(input("Enter two Number:  ")),int(input()))