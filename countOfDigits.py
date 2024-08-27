number = int(input('Enter a number to count no. of digits'))
number_str = str(number)
digit_count = 0

for char in number_str:
    if char.isdigit():
        digit_count += 1

print(digit_count)