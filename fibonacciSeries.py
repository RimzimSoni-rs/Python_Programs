n = int(input("Enter the number of terms : "))
x = 0
y = 1
i = 0
print(x)
print(y)

while(i <=n):
    
    print(x + y)
    temp = x
    x = y
    y = temp + y 
    i+=1
   