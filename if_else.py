number = int(input("Enter a number: "))


#find even-odd
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

#find prime-number
count=0
for i in range (1,10):
    if number%i ==0:
      count=count+1 
if number ==0:
    print("Zero is not a prime number")
      
if count >2: 
      print ("It is not a prime number")
else:
   print("number is prime")
