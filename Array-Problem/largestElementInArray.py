def largestElementInArray(arr):
    return max(arr)


arr=list(map(int,input("Enter element in Array : ").split()))
res=largestElementInArray(arr)
print(f"Largest element in Array {arr} = {res}")