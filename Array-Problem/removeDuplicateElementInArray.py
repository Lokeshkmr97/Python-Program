def removeDuplicateElementInArray(arr):
    temp=[]
    for i in arr:
        if i not in temp:
            temp.append(i)
    return temp


ar=list(map(int,input("Enter Element in Array : ").split()))
res=removeDuplicateElementInArray(ar)
print(f"After removing Duplicate element from an array is {res}")