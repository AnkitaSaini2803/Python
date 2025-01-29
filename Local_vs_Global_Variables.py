''' 15/1/2025
A local variable is a variable that is defined within a function 
and is only accessible within that function. It is created when 
the function is called and is destroyed when the function returns.
'''
x=6    #Global variable
def function():
    x=10
    print(x)    #inside the function :Local Variable
function()
print(x)
# print(y) Error is generated in this line bec. y has no scope ouside the function 

'''
 global variable is a variable that is defined outside of a function 
 and is accessible from within any function in your code.
 The global keyword is used to declare that a variable is a global
 variable and should be accessed from the global scope.
'''
x=6    #Global variable
def function():
    global x
    x=89      # this will change the value of the global variable x
    print(x)    #inside the function :Local Variable
function()
print(x)
