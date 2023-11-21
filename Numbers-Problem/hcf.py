def findHCF(n1,n2):
    mx=max(n1,n2)
    hcf=1
    for i in range(1,mx+1):
        if n1%i==0 and n2%i==0:
            hcf=i
    return hcf


n1=int(input("Enter first Number : "))
n2=int(input("Enter second Number : "))

res=findHCF(n1,n2)
print(f"HCF of Two Number {n1} and {n2} is {res}")