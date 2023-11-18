def checkArmstrongNumber(num):
    sm=0
    temp=num
    while temp>0:
        sm+=(temp%10)**3
        temp//=10
    if sm==num:
        return True
    else:
        return False
    
def printAllArmstrongNumberBetweenGivenRange(l,r):
    for i in range(l,r+1):
        if checkArmstrongNumber(i)==True:
            print(i,end=" ")
            
left=int(input("Enter Left Range : "))
right=int(input("Enter Right Range : "))
printAllArmstrongNumberBetweenGivenRange(left,right)