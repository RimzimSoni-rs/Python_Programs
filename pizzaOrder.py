print("-----AUTOMATIC PIZZA ORDERING PROGRAM-----")
a="small pizza"
b= "medium pizza"
c="Large pizza"
prize =0
print("\nOptions available for pizzas:\nSmall Pizza\nMedium Pizza\nLarge Pizza")
pizza = input("Enter the size of pizza you want : ")
if pizza == a:
    prize+=100
elif pizza ==b:
    prize+=200
elif pizza == c:
    prize+=300
else: 
    print("enter correct size for pizza")

if pizza==a or pizza==b or pizza==c:
 extra =input("Do you want to add pepperoni ??  enter y/n : ")
 if extra == "y":
  if pizza == a:
    prize+=30
  if pizza ==b or pizza == c :
    prize+=50

cheese = input("Do you want extra cheese?? enter y/n : ")
if cheese =='Y' or cheese =='y':
   prize+=50
 
   

print("you have ordered a ", pizza, "and your bill is : ", prize)


