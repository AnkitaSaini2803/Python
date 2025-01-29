'''             10/1/2025
Doc strings are string literals that appear right after the 
function definition,class ,module
'''
def square(n):
    '''Takes a number n and return its square,this is 
     a docstring '''
    print(n**2)
square(10)
print(square.__doc__)    #This will print the docstring

def sum_of_numbers(a,b):
    '''Takes two numbers a and b and find out the sum of two
      numbers a+b'''
    return a+b
num_1=int(input("Enter first Number: "))
num_2=int(input("Enter the second Number"))
print(num_1,num_2)
print(sum_of_numbers(num_1,num_2))


def sum_of_numbers(a,b):
    '''Takes two numbers a and b and find out the sum of two
      numbers a+b'''
    print(a+b) 
a=int(input("Enter first Number: "))
b=int(input("Enter the second Number"))
sum_of_numbers(a,b)   
print(sum_of_numbers.__doc__)


def sum(a,b):
    '''Takes two numbers a and b and find out the sum of two
      numbers a+b'''
    print(a+b) 
num_1=int(input("Enter first Number: "))
num_2=int(input("Enter the second Number"))
print(num_1,num_2)
sum(num_1,num_2)
print(sum.__doc__)

'''
PEP 8
PEP 8 is a document that provides guidelines and best practices on how to 
write Python code. It was written in 2001 by Guido van Rossum, Barry Warsaw
, and Nick Coghlan. The primary focus of PEP 8 is to improve the readability
 and consistency of Python code.

PEP stands for Python Enhancement Proposal, and there are several of them.
 A PEP is a document that describes new features proposed for Python and 
 documents aspects of Python, like design and style, for the community.

'''
