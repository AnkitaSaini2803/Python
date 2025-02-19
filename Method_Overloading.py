'''                                                             16-2-2025
There is no Method overloading in python like other languages like C++. But it can 
be achieved in two ways:
1. Inefficient - Using Multiple functions with same name .But only last function
will be considered and rest will not be considered (hidden)

2. Efficient - Using multiple dispatch decorator 
'''

def mul(a):
    return a*a
 
def mul(a,b):
    return a+b

def mul(a,b,c):
    return a*b*c

# print(mul(5,6)) #This will show an error
# print(mul(5,6))
print(mul(5,6,2))


# 2. Using multiple dispatch decorator
from multipledispatch import dispatch 
@dispatch(int,int)
def fun(a,b):
    return a*b

@dispatch(int,int)
def fun(a,b):
    return a+b
    
@dispatch(int,int,int)
def fun(a,b,c):
    return a*b*c

print(fun(5,6))
print(fun(5,6))
print(fun(5,6,2))