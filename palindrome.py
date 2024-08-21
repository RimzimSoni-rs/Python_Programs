
user_input = input("Enter a string to check if it's a palindrome: ")

cleaned_string = ''.join(user_input.split()).lower()

cleaned_string = ''.join(c for c in cleaned_string if c.isalnum())

if cleaned_string == cleaned_string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
