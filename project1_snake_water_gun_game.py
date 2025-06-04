import random


def user1(comp,player):
   if comp=="s" and player =="s":
      return "draw"
   
   if comp=="w" and player =="w":
      return "draw"
   
   if comp=="g" and player =="g":
      return "draw"
   
   if comp=="s" and player =="w":
      return "com wins"
   
   if comp=="s" and player =="g":
      return "player wins"
   
   if comp=="w" and player =="s":
      return "player wins"
   
   if comp=="w" and player =="g":
      return "comp wins"
   
   if comp=="g" and player =="w":
      return "player wins"
   
   if comp=="g" and player =="s":
      return "comp wins"
   
   
print("computer's turn to choose between snake(s), water(w), gun(g)")
comp1=random.randint(1,3)
if(comp1==1):
    comp ='s'
elif(comp1==2):
    comp ='w'
elif(comp1==3):
    comp ='g'

player=input("player's turn: choose between snake(S), water(W), gun(G) \n")
a=user1(comp,player)
print(f"you choose: {player}")
print(f"computer choose: {comp}")
print(a)         