def checkPalindromeNumber(num):
    temp=num
    rev=0
    while temp>0:
        rev=rev*10+temp%10
        temp//=10
    if rev==num:
        return "Palindrome Number "
    else:
        return "Not Palindrome Number "
    
n=int(input("Enter Any Number : "))
res=checkPalindromeNumber(n)
print(f"{n} is {res}")