'''        12/1/2025
Raising custom errors in python using raise keyword'''
num=int(input("Enter the value between 5 to 10:"))
print(num)
if(num<5 or num>10):
    raise ValueError("The number entered is not between 5 to 10")

a = int(input("Enter any value between 5 and 9"))

if(a<5  or a>9):
  raise  ValueError("Value should be between 5 and 9")

''' QUICK QUIZ
num=input("Enter value")
if(num!='quit'  num!=int(num)):
    raise ValueError("The value entered is neither quit nor integer")
else:
  
 print(num)
   
 '''