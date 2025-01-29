''' 16/1/2025
Making the Game : Snake Water Gun'''

name=input("Enter Your Name before starting the Game :")
print(f"{name} vs computer")
print("Choose any one option: 0 for snake,1 for water and 2 for gun")
player=int(input("Enter Your Choice:"))

import random
computer=random.randint(0,2)
print("Computer chooses" ,computer)

if(player==0 and computer==0  or player==1 and computer==1 or player==2 and computer==2):
    print(f"There is draw between {name} and computer")
elif(player==0 and computer==1 or player==1 and computer==2 or player==2 and computer==0):
    print(f"{name} win against computer")
elif(player==0 and computer==2 or player==1 and computer==0 or player==2 and computer==1):
    print(f"Computer win against {name}")
print(computer)
print("Thanks for participating")
    