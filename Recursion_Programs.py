'''            10/1/2025       HAPPY PUTRADA EKADASHI
1. Write a program to find factorial of a number using recursion
'''
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
i=0
for i in range(0,10):
    print("Factorial of",i,"is :",factorial(i))
     
'''
2. Write a Program to find FIBONACCI sequence 0,1,1,2,3,5,8,13,21,34,.......
'''
# Method 1       T.C = O(2^n)
def fibonacii(n):
    if(n==0):
        return 0
    elif (n==1):
        return 1
    else:
        return fibonacii(n-1)+fibonacii(n-2)
print("Value in fibanacci sequence at index 6 is:",fibonacii(6))
i=0
for i in range(0,15):
    print("Value in fibanacci sequence at index ",i,"is:" ,fibonacii(i))

# Method 2         (Memoization) T.C = O(n)
import functools
@functools.lru_cache(maxsize=None)
def fibonacciNumber(N):
    # Write your code here.
    if N==0:
        return 0
    if N==1:
        return 1
    else:
      return fibonacciNumber(N-1)+fibonacciNumber(N-2)
print(fibonacciNumber(8))

#Method 3
n=int(input("Enter : "))
def fib(n):
    a,b=0,1
    if n<2:
        return n
    
    for _ in range(2,n+1):
        a,b = b,a+b
    return b
N=print(fib(n))