# OLD WAY OF STRING FORMATING IN PYTHON using format method
letter="Hey,My name is {} and I am From Country {}"
name='Ankita'
country='INDIA'
print(letter.format(name,country))
print(letter.format(country,name))

# letter="Hey,My name is {1} and I am From Country {0}"
# print(letter.format(country,name))
'''
#It is new string formatting mechanism introduced by the PEP 498. 
# It is also known as Literal String Interpolation or
#  more commonly as F-strings (f character preceding the string literal). 
# The primary focus of this mechanism is to make the interpolation easier.
'''

print(f"Hey,my name is {name} and i am from {country}")
print(f"Hey,my name is {{name}} and i am from {{country}}")

# .3f upto 3 decimal positions and .2f upto 2 decimal positions
text=90.34122
print(f"hey the amount {text:.3f} is in dollars")

val = 'Geeks'  
print(f"{val}for{val} is a portal for {val}.")  

print(f"{2 * 30}")