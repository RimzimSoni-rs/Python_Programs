#Using break to exit a loop when a condition is met

print("Finding the first number greater than 5:")
for i in range(10):
    if i > 5:
        print(f"Found number greater than 5: {i}")
        break  
    print(f"Current number: {i}")


#Using continue to skip even numbers

print("Odd numbers between 1 and 10:")
for i in range(1, 11):
    if i % 2 == 0:
        continue  
    print(i)
