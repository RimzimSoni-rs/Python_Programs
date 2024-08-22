n = int(input('Enter number to print pattern lines: '))
print('Printing Right triangle\n')
for i in range(n):
    print('*' * (i + 1))

print('Printing Equilateral triangle\n')
for i in range(n):
    print(' ' * (n - i - 1) + '*' * (2 * i + 1))

print('Printing Diamond pattern\n')
  
for i in range(n):
    print(' ' * (n - i - 1) + '*' * (2 * i + 1))
   
for i in range(n - 2, -1, -1):
    print(' ' * (n - i - 1) + '*' * (2 * i + 1))

