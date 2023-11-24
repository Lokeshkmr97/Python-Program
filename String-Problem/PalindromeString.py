def checkPalindromeString(st):
    if st==st[::-1]:
        return "Palindrome String"
    else:
        return "Not Palindrome String"

s=input("Enter Any String : ")
res=checkPalindromeString(s)
print(f"String is {res}")