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
