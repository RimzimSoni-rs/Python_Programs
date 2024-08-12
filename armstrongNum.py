num = int(input("Enter number to check : "))
temp = num
sum = 0
num_str = str(num)  # Convert the number to a string
num_length = len(num_str)  # Get the length of the string

while temp > 0:
    sum += (temp % 10) ** num_length
    temp //= 10  # Remove the last digit

if sum == num:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
