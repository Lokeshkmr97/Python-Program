def sumOfDigitOfNumber(n):
    sm=0
    while n>0:
        d=n%10
        sm+=d
        n//=10
    return sm

num=int(input("Enter Any Number : "))
res=sumOfDigitOfNumber(num)
print(f"Summation of digit of a Number {num} ={res}")