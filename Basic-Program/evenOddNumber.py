def checkEvenOddNo(n):
    if n%2==0:
        return "Even Number"
    else:
        return "Odd Number"

n=int(input("Enter any Number : "))
res=checkEvenOddNo(n)
print(f"{n} is {res}")