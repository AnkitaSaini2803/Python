# FUNCTION ARGUMENTS TYPES              8/1/2025
# DEFAULT ARGUMENTS
def find_average(a=5,b=2):
    average=(a+b)/2
    print(average)
find_average(7,3)    

def find_average(a=5,b=2):
    average=(a+b)/2
    print(average)
find_average()    

def find_average(a=9.255,b=5.5):
    average=(a+b)/2
    print(average)
find_average()

def name(f_name,m_name='Saini',last_name='Ji'):
      print('Hello,',f_name,m_name,last_name)
name('Ankita')     

# KEYWORD ARGUMENTS : Arguments are recognized based on parameter
# name by the interpreter and order of arguments doesnot matter
def name(f_name,m_name,last_name):
     print(f_name,m_name,last_name)
name(last_name='watson',f_name='Hello',m_name='john') 

# VARIABLE-LENGTH ARGUMENTS
def find_average(*numbers):
     sum=0
     print(type(numbers))
     for i in numbers:
          sum=sum+i
          print("Average is:",sum/len(numbers))
find_average(3,4,5,1,2,6,7,8,9,10)          
    
# RETURN STATEMENT


def sum(a,b,c):
     return a+b+c
num1=int(input("Enter first number"))
num2=int(input("Enter second number"))
num3=int(input("Enter third number"))

print(sum(num1,num2,num3)) 
