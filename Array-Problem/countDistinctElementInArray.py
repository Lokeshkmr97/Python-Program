def countDistinctelementInArray(arr):
    disArr=[]
    for i in arr:
        if i not in disArr:
            disArr.append(i)
    return len(disArr)


ar=list(map(int,input("Enter Element in Array : ").split()))
res=countDistinctelementInArray(ar)
print(f"Total distinct element in array {ar} ={res}")