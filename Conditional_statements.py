# If else statement                                       3/1/2025

a=int(input("Enter the number: "))
print(a)
if(a>=18):
    print("You are eleigible to vote")
else:
    print("Sorry,You are under age")
print('Thank You')   

# Elif conditions

price=int(input("Enter the price : "))
print(price)
budget=200
if(budget<price):
    print("Sorry,we can't help")
elif(budget-price>80):
    print("Take 1 KG of apples")
    print("Change will be given through Cash")
elif(budget==price):
    print("Yayyy....,you can take Apples with you")
else:
    print("Sorry")   
print("Thanks for coming in our shop")

# Nested if else statement

num=int(input())
print("Enter the number",num)
if(num<0):
    print("The number is negative")
elif(num>0):
    if(num<=10):
        print("The number lies between 0 and 10")
    elif(num>10 and num<=20):
        print("The number lies between 11 to 20")
    else:
        print("Number is greater than 20")
else:
    print("Number is Zero")  


'''  One line if else statement           13/1/2025'''
age=int(input("Enter the age"))
print("You can Vote") if age>=18 else print('No You Cant')

Cgpa=int(input("Enter Your Marks:"))
print("You are first in class Ankita ,Congratulations!") if Cgpa>=90 else print('''"You are Hardworking Girl and I know you'll achieve someting big in life and make 
your parents proud"''')