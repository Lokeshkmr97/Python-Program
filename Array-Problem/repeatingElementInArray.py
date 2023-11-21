def repeatingElementInArray(arr):
    rept=[]
    for i in arr:
        if arr.count(i)>1:
            rept.append(i)
    return list(set(rept))

arr=list(map(int,input("Enter Element in Array : ").split()))
res=repeatingElementInArray(arr)
print(f"Repeating Element in an Array {arr} = {res}")