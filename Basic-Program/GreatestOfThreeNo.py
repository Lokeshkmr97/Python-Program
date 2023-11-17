def GreatestOfThreeNo(n1,n2,n3):
    if n1>n2 and n1>n3:
        return n1
    elif n2>n3:
        return n2
    else:
        return n3
    
n1=int(input("Enter any No. : "))
n2=int(input("Enter any No. : "))
n3=int(input("Enter any No. : "))
res=GreatestOfThreeNo(n1,n2,n3)
print(f"Greatest is {res}")