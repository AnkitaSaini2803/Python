'''1. WAP to print this pattern                                       11/2/2025
*****
*****
*****
*****   '''
for i in range(1,6):
    for j in range(1,6):
        print("*",end='')
    print()

print("\n")

'''2. WAP to print this pattern 
*    
**   
***  
****
*****  
Code 1 is better in terms of efficiency and simplicity since it avoids an
unnecessary nested loop.
Code 2 is useful if you want more control over formatting, like adding spaces 
between asterisks
'''
#solution 1
for i in range(1,6):
    print("*"*i)
print()

#solution 2
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")   
    print()    