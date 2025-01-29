# Making calculator                       31/12/2024
'''
a=5
b=10
print("Addition of two numbers",a+b)
print("Subtraction of two numbers",a-b)
print("Multiplication of two numbers",a*b)
print("Division of two numbers",a/b)
print("Exponential operator",a**b)

'''
# Taking input Using Input Function

a=input("Enter First Number: ")
b=input("Enter Second Number: ")
# print("The result after addition is:",a+b) Here result was concatenating both 
# strings bec input func take everything as an input so u need to do tyecasting
print("The result after addition is:",int(a)+int(b))
print("The result after Subtraction is :",int(a)-int(b))
print("The result after Multiplication is",int(a)*int(b))

x=input("Enter First Number: ")
y=input("Enter Second Number: ")
print("The result after addition is:",float(x)+float(y))
print("The result after Subtraction is :",float(x)-float(y))
print("The result after Multiplication is",float(x)*float(y))

