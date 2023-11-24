def captalizeFirstCharacter(st):
    lst=list(st.split())
    capSt=''
    for i in lst:
        capSt+=i[0].upper()+i[1:]+" "
    print(capSt) 



str=input("Enter any String : ")
captalizeFirstCharacter(str)
