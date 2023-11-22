st=input("Enter any String : ")
vowel=[]
for i in st:
    if i in 'aeiouAEIOU':
        vowel.append(i)
print(f"Total Number of Vowel in this String is {len(vowel)} and {list(set(vowel))}")