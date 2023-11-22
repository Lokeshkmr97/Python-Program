def findLCM(n1,n2):
    # (formula lcm*hcf=product of two number)
    res=findHCF(n1,n2)
    lcm=n1*n2//res
    return lcm
    
def findHCF(n1,n2):
    mx=max(n1,n2)
    hcf=1
    for i in range(1,mx+1):
        if n1%i==0 and n2%i==0:
            hcf=i
    return hcf


n1=int(input("Enter First Number : "))
n2=int(input("Enter Second Number : "))
result=findLCM(n1,n2)
print(f"LCM of Two Number {n1} and {n2} is {result}")

