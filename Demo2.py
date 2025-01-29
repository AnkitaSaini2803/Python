#Day 2   Data-types + Operator + TypeCasting             31/12/2024
a=10         #'int'
b="Python"    # str
c=False       #'bool'
d=4.44         #'float'
print(a)
print(type(a))      #type() is used to know the datatype of any variable
print(b)
print(type(b))
print(c)
print(type(c))
print(d)
print("The datatype of d is ",type(d))
e=complex(5,4)     #complex number
print(e, type(e))

x="Saini"
y=" Ji "
print(x+y)     #Saini Ji

w="1"
z='2'
print(w+z)     #12

#Explicit Type Casting in python
print(int(w)+int(z))    #Done manually by programmer

# Implicit Type castsing in python
print(a+d)       #Done by python interpreter


'''24/1/2025          we can declare a variable using any alphabet and also using
underscore(_) not numeric term'''
_='string'
print(type(_),_)