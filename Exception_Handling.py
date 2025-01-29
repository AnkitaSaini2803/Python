''' 12/1/2025
EXCEPTION HANDLING USING TRY AND EXCEPT'''
try:
   num=int(input("Enter the number"))
   for i in range(1,11):
      print(f"The multiplication table of {num} is {num}*{i} ={num*i}")
except :
   print("The entered number is not an integer")


try:
   num1=int(input("Enter the value:"))
   list=[3,4,1]
   print(list[num1])
except ValueError:
   print("The entered number is not an integer")
except IndexError:
   print("Index Error")  

''' USING FINALLY CLAUSE WITH TRY AND CATCH IN EXCEPTION HANDLING'''

def func():
   try:
     number=int(input("Enter the value:"))
     l=[1,5,8,0]
     print(l[number])
     return 1
   except:
      print("Some Invalid Error occurs")
      return 0
   
# print("Print this last line")      line will not be printed
   finally:
    print("I AM ALWAYS EXECUTED")
x=func()
print(x)
'''
x=func()
print(x)
print("Print this last line,it is required")
like this,lastt line will be printed 
'''
# 23/1/2025
def foo():
    try:
        return 1
    finally:
        return 2

#Driver's code
k = foo()
print(k)

#24/1/2025    here error will come because x is not defined
try:
    print(x)
except:
    print("An exception occurred")

