print("\n---LOVE CALCULATOR----")
name1= input("Enter your name : ")
name2= input("Enter your partner's name : ")
score = 0
n1 = name1.lower() 
n2 = name2.lower()
combine = n1 + n2

t = combine.count('t')
r = combine.count('r')
u = combine.count('u')
e = combine.count('e')
true = t + r + u + e

l = combine.count('l')
o = combine.count('o')
v = combine.count('v')
e = combine.count('e')
love = l + o + v + e

score = str(true) + str(love)

if int(score) < 10 or int(score) > 90:
    print(f"Your score is {score} and you go together like coke and mentos")

elif int(score) >=40 and int(score) <= 50:
    print(f"Your score is {score} and you are alright together")
else:
     print(f"Your score is {score}")

 



    