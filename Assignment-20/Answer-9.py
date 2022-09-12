def isPangram(s):
    for e in s:
        if (ord(e)>=65 and ord(e)<=97) or (ord(e)>=97 and ord(e)<=122) or ord(e)==32:
            pass
        else:
            return False
    else:
        return True


print("Pangram String" if isPangram(input("Enter a String: ")) else "Not Pangram String")