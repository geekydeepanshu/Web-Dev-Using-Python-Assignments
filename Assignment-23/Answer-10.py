def coPrime_hcf(hcf):
    def coPrime(a,b):
        if hcf(a,b)==1:
            print("Co-Prime Numbers")
        else:
            print("Not Co-Prime Numbers")
            return hcf(a,b)
    return coPrime_hcf
@coPrime_hcf
def hcf(a,b):
    c=a if a>b else b
    for e in range(c,0,-1):
            if a%e==0 and b%e==0:
                return e

print("HCF of given Numbers is: ",hcf(2,4))
