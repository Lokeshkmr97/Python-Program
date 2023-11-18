def primeNumberBetweenRange(l,r):
    for i in range(l,r+1):
        if checkPrimeNo(i)==True:
            print(i,end=" ")
    

def checkPrimeNo(n):
    flag=0
    if n<2:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            flag=1
            break
    if flag==1:
        return False
    if flag==0:
        return True
    
left=int(input("Enter left range : "))
right=int(input("Enter right range : "))
primeNumberBetweenRange(left,right)