''' 15/1/2025
A lambda function is a small anonymous function without a name.
It is defined using the lambda keyword and has the following syntax:

                lambda arguments: expression
 Lambda functions are often used in situations where a small function 
 is required for a short period of time. They are commonly used as arguments
 to higher-order functions, such as map, filter, and reduce.
'''
def cube():
    x=int(input("Enter number:"))
    print(f"{x**3}")
cube()
'''SAME SAME BUT DIFFERENT'''
cube=lambda x:x*x*x
print(cube(9))

def func(fx,value):
    return 6+fx(value)
print(func(cube,4))
