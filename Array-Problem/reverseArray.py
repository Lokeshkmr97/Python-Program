def reverseArrayElement(arr):
    tempArray=arr
    start=0
    end=len(arr)-1
    while start<end:
        temp=arr[start]
        arr[start]=arr[end]
        arr[end]=temp
        start+=1
        end-=1
    return tempArray,arr

arr=list(map(int,input("Enter Element in Array : ").split()))
originalArray,res=reverseArrayElement(arr)
print(f"Original Array Element {originalArray} and Reverse Array element {res}")