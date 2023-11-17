def checkLeapYear(yr):
    if (yr%400==0) or (yr%4==0 and yr%100!=0):
        return "Leap Year"
    else:
        return "Not Leap Year"
    
year=int(input("Enter Any Year : "))
res=checkLeapYear(year)
print(f"{year} is {res} ")