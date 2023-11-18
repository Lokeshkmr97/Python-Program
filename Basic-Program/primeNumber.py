def checkPrimeNumber(n):
    flag=0
    for i in range(2,n//2+1):
        if n%i==0:
            flag=1
            break
    if flag==0:
        return "Prime Number"
    if flag==1:
        return "Not Prime Number"
    
n=int(input("Enter Any Number : "))
res=checkPrimeNumber(n)
print(f"{n} is {res}")