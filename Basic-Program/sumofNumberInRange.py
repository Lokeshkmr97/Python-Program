def sumOfNumberInGivenRange(l,r):
    sm=0
    for i in range(l,r+1):
        sm+=i
    return sm

n1=int(input("Enter any Number : "))
n2=int(input("Enter any Number : "))
res=sumOfNumberInGivenRange(n1,n2)
print(f"Sum of given range {n1} and {n2} is {res}")