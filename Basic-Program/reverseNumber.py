def reverseNum(n):
    rev=0
    while n>0:
        temp=n%10
        rev=rev*10+temp
        n//=10
    return rev

num=int(input("Enter any Number : "))
res=reverseNum(num)
print(f"{num} reverse number is {res}")