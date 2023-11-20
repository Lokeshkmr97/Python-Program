def countElementInArray(arr):
    d={}
    for i in arr:
        d[i]=0
    for j in arr:
        d[j]+=1
    return d


ar=list(map(int,input("Enter element in Array : ").split()))
res=countElementInArray(ar)
print(f"Total Frequency of the element in Array is {ar} = {res}")