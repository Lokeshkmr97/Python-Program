char=input("Enter any Character : ")
if len(char)>1:
    print("Please enter only a single Character (not More than one Character)")
else:
    print(f"The Ascii Value of Character {char} is {ord(char)}")