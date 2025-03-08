'''14/2/2025
8. Print the Inverted Pyramid Pattern
*********
 *******
  *****
   ***
    *
'''
n=5
for i in range(n,0,-1):
    print(' '*(n-i)+"*"*(2*i-1))

'''
9. Print the Diamond Pattern 
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
'''
print("\n")

n=5
for i in range(n):
        print(' '*(n-i-1) + "*" *(2*i+1))
for i in range(n-1,0,-1):
    print(' '*(n-i)+"*"*(2*i-1))

'''10. Print the Right Arrow pattern 
    
*
**
***
****
*****
****
***
**
*
'''

n=5
for i in range(n+1):
      print("*"*i)
for i in range(n-1,0,-1):
      print("*"*i)

'''11. Print the Left Arrow pattern 
    *
   **
  ***
 ****
*****
 ****
  ***
   **
    *
'''
n=5
for i in range(1,n+1):
    print(' '*(n-i)+"*"*i)
for i in range(n-1,0,-1):
     print(' '*(n-i)+"*"*i)

'''12.  Print the following pattern                                     15/2/2025
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
'''
n=5;num=1
for i in range(1,n+1):
    for j in range(0,i):
        print(num,end=" ")
        num+=1
    print()

'''13. Diagonal Pattern
    *
   *
  *
 *
*
'''
n=5
for i in range(0,n):
    print(' '*(n-i-1)+"*")

'''14. Diagonal Pattern
*
 *
  *
   *
    *
'''
print("\n")

n=5
for i in range(0,n):
    print(' '*(i)+"*")

'''15. Staircase Pattern (Ascending)
     # 
    #  #
   #  #  #
  #  #  #  #
 #  #  #  #  #
'''
n=5
for i in range(1,n+1):
    print(' ' * (n-i) + " # " * i)

for num in range(2,5,1):
    print(num, end=" ,")

'''16. Cross-Pattern 
*           * 
  *       *   
    *   *
      *
    *   *
  *       *
*           * 
'''
# First Solution                                                   16-2-2025
n=7
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()
print("\n")
# Second Solution 
for i in range(n):
    for j in range(i):
        if i==j or j==n-i-1:
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()

