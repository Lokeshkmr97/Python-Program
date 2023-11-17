def GreatestOfTwoNo(n1,n2):
    if n1>n2:
        return n1
    else:
        return n2
n1=int(input("Enter any No. : "))
n2=int(input("Enter any No. : "))
res=GreatestOfTwoNo(n1,n2)
print(f"Greatest Number is {res}")