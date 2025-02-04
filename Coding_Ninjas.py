'''31/1/2025
1.Write a program that takes a character as input and prints 1, 0, or -1 according 
to the following rules.
1, if the character is an uppercase alphabet (A - Z).
0, if the character is a lowercase alphabet (a - z).
-1, if the character is not an alphabet.
'''
# solution1           O(n)
import string
text=input()
if len(text)!=1:
    raise ValueError("Enter single character only")
lowercase=string.ascii_lowercase
uppercase=string.ascii_uppercase
if text in lowercase:
    print('0')
elif text in uppercase:
    print('1')
else:
    print('-1')

#solution2            O(1)
text=input()
if text.islower():
    print('0')
elif text.isupper():
    print('1')
else:
    print('-1')

#solution3           O(1)
text=input()
if text>='a' and text<='z':
    print('0')
elif text>='A' and text<='Z':
    print('1')
else:
    print('-1')

'''2.
Write a program that takes three numbers a,b, and c as input and 
prints the largest number amongst them.
Detailed explanation ( Input/output format, Notes, Images )
'''
a,b,c=map(int,input("Enter values").split())

if a>b and a>c:
    print(a)
elif b>=a and b>c:
    print(b)
elif c>a and c>b:
    print(c)

'''3.'''
from typing import *
from math import pi

def areaSwitchCase(ch: int, a: List[float]):
   if ch==1:
       return f"{pi*a[0]*a[0]:.5f}"
   elif ch==2:
        return f"{a[0]*a[1] :.5f}"
print(areaSwitchCase(1,[7]))
print(areaSwitchCase(2,[2,3]))

'''4.                       4/2/2025
Given a number N, print sum of all even numbers from 1 to N.
'''
# solution 1
number=int(input("Enter"))
sum_even=0
for i in range(1,number+1):
 if i%2==0:
   sum_even+=i
print(sum_even)

#solution 2        
number=int(input("Enter"))
sum_even=0
for i in range(2,number+1,2):
   sum_even+=i
print(sum_even)

'''5. Write a program to find x to the power n (i.e., x^n). Take x and n from the
user. You need to print the answer.Note: For this question, you can assume that 0 
raised to the power of 0 is 1
'''         
x,n=map(int,input("Enter values of x and n:").split())
if x<=8 and n<=9:
 if x==1 and n==0:
  print('1')
 else:
  print(x**n)

