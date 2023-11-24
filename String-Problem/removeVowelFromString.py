def removeVowelFromString(st):
    newSt=''
    vowels='aeiouAEIOU'
    for i in st:
        if i not in vowels:
            newSt+=i
    return newSt

s=input("Enter any String : ")
res=removeVowelFromString(s)
print(f"Original String is ({s}) and After Removing All Vowels from String is ({res})")
