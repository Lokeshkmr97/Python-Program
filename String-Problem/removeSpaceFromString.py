def removeSpaceFromString(st):
    newSt=''
    for i in st:
        if i not in " ":
            newSt+=i
    return newSt


str=input("Enter any String : ")
res=removeSpaceFromString(str)
print(f"After removing Space from String is {res}")