''' 12/2/2025
Solution 1
'''
import re
string_input=input("Enter String :")
expression=r"[^A-Za-z0-9]+"
final=re.sub(expression,'',string_input).lower()
for i in range(0,len(final)//2):
    if final[i]==final[len(final)-i-1]:
        print("Yes")
    else:
        print("No")
'''
Solution 2                                     
'''
from os import *
from sys import *
from collections import *
from math import *
import re

def checkPalindrome(s):
    # Write your code here
	# Return a boolean
	expression=r"[^A-Za-z0-9]"
	output=re.sub(expression,"",s).lower()
	for i in range(len(output)//2):
		if output[i]!=output[len(output)-i-1]:
			return False
	return True


