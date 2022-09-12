def isPalindrome(s):
    return True if s==s[::-1] else False

print("Yes" if isPalindrome(input("Enter a String: ")) else "No")