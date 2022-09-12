def isAnagram(str1, str2):
    l1=list(str1)
    l2=list(str2)
    l1.sort()
    l2.sort()
    return True if l1 == l2 else False


print("Anagram String" if isAnagram(input("Enter First String: "),input("Enter Second String: ")) else "Not Anagram String")

