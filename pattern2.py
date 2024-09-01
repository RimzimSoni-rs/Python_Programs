height = int(input("Enter no of rows: "))
for i in range(height, 0, -1):
    print(' ' * (height - i), end='')
      
    print('*' * (2 * i - 1))

