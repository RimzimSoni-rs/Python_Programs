n = 1
prime_flag = 0

if(n > 1):
    for i in range(2, int(n**2) + 1):
        if (n % i == 0):
            prime_flag = 1
            break
    if (prime_flag == 0):
        print("True")
    else:
        print("False")
else:
    print("False")
