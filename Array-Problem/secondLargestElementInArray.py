def secondLargestElementInArray(arr):
    n=len(arr)
    arr.sort()
    return arr[n-2]

arr=list(map(int,input("Enter Element in Array : ").split()))
res=secondLargestElementInArray(arr)
print(f"Second Largest Element in Array {arr} = {res}")