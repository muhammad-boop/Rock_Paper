import random
"""
Rock Paper Scissors Game in python
r = 1
p  = 0
s = -1
"""
computer = random.choice([0, 1, -1])
youstr = input("Enter Your Choice: ")
youDict = {"r":1, "p":-1, "s":0}
reversedDist = {1:"Rock",0:"Scissors", -1:"Paper"}
you = youDict[youstr]
print(f"You have chosed {reversedDist[you]} and computer has chosed {reversedDist[computer]}")
if(computer == -1 and you==1):
  print("You Won!")
elif(computer == -1 and you==0):
  print("Computer Won!")
elif(computer == -1 and you==-1):
  print("Draw!")
elif(computer == 1 and you==-1):
  print("Computer Won!")
elif(computer ==1 and you==0):
  print("You Won!")
elif(computer == 1 and you==1):
  print("Draw!")
elif(computer== 0 and you==1):
  print("Computer Won!")
elif(computer ==0 and you==-1):
  print("You Won!")
elif(computer ==0 and you==0):
  print("Draw!")