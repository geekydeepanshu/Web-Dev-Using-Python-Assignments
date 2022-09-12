def stringCaseCounter(l=[]):
    uc, lc = 0, 0
    for e in l:
        if ord(e) >= 65 and ord(e) <= 90:
            uc += 1
        if ord(e) >= 97 and ord(e) <= 122:
            lc += 1
    return uc, lc


uc, lc = stringCaseCounter(list(input("Enter a String: ")))
print("Number of Lowercase letter in given string is {} and Number of Uppercase letter in given string is {}".format(lc,uc))
