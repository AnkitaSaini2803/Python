'''The generator is used to generate the values one-by-one as the loop iterates
over it.       25/1/2025
'''
def generator():
    for i in range(30):
        yield i
obj=generator()
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))

for j in obj:
    print(j)

'''Function Caching '''
import functools
@functools.lru_cache(maxsize=None)
def fib(n):
    if(n==0):
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

print(fib(8))