def checkArmstrongNumber(num):
    sm=0
    temp=num
    while temp>0:
        sm+=(temp%10)**3
        temp//=10
    if sm==num:
        return "Armstrong Number "
    else:
        return "Not Armstrong Number "


n=int(input("Enter Any Number : "))
res=checkArmstrongNumber(n)
print(f"{n} is {res}")