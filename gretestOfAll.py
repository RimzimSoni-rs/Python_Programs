a =int(input("Enter 1st number"))
b =int(input("Enter 2nd number"))
c =int(input("Enter 3rd number"))
if a>b:
    if a>c:
        print(f'{a} is largest number')
    else:
        print(f'{c} is largest')
else:
    print(f"{b} is largest")