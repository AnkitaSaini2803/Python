'''Decorators                       16/1/2025'''
def greet(fx):
    def mfx(*arg,**args):
        print("Good Morning")
        fx(*arg,*args)
        print("Thanks for calling this function")
    return mfx
    
@greet
def hello():
    print("Hello World")
hello()

@greet
def add(a,b):
    print(a+b)
add(6,6)