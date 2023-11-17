def checkPosNegNo(n):
    if n>0:
        return "Positive Number"
    else:
        return "Negative Number"

n=int(input("Enter any number : "))
res=checkPosNegNo(n)
print(f"{n} is {res}")