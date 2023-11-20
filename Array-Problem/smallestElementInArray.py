def smallestElementInArray(arr):
    return min(arr)


arr=list(map(int,input("Enter element in Array : ").split()))
res=smallestElementInArray(arr)
print(f"Smallest element in Array {arr} = {res}")