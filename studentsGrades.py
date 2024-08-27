percentage = int(input('Enter your percentage: '))
if percentage >=90:
    print("O Grade")
elif percentage >=80:
    print("A Grade")
elif percentage >=70:
    print("B Grade")
elif percentage >=60:
    print("C Grade")
elif percentage >=50:
    print("D Grade")
elif percentage<40 and percentage>35:
    print("Pass")
else :
    print("Fail")
