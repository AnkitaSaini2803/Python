'''1. Print Solid Square Pattern                                      11/2/2025
*****
*****
*****
*****   '''
for i in range(1,6):
    for j in range(1,6):
        print("*",end='')
    print()

print("\n")

'''2. WAP to print Right-angled Triangle Pattern (Left)
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
    print(" * "*i)
print()

print("\n")

#solution 2
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")   
    print()    

print("\n")
# 3...........
count=4
for i in range(1,5):
    for j in range(1,count+1):
     print("*"*count)
     count=count-1

# second one is better and first code is not recommended             12/2/2025
count=4
for i in range(count,0,-1):
    for j in range(i):
        print('*',end=" ")
    print()


print("\n")
                                                                     #13/2/2025 
''' 4. Print this pattern
1
12
123
1234
12345
'''
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
            print(j,end="")
    print()

''' 5. 
54321
4321
321
21
1

'''
print("\n")
n=5
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end="")
    print()

'''6.
12345
1234
123
12
1
'''
print("\n")

for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()

'''7 Print the Pyramid Pattern 
    *
   ***
  *****
 *******
*********
'''
n=5
for i in range(n):
        print(' '*(n-i-1) + "*" *(2*i+1))



'''ALSO WATCH OUT THIS QUESTION'''

def printPattern(n):
    if n == 1:
        print('*')
    else:
        for i in range(n): 
            print(('*'*(2*i+1)).center(2*n-1, ' '))

