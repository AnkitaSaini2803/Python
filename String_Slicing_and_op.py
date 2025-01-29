# STRING SLICING AND STRING METHODS                      1/1/2025
# 14/1/2025

r='Hello'
result=r[::-2]
print(result)
s = "AnkitaSaini"
#  rev = s[::1]
rev = s[::-1]
# rev=s[:-1]
print(rev)


string="Mango Is Tasty"
display=len(string)
print(display)
print(type(display))
print(type(string))
print(string[0:])
print(string[0:5]) #include 0 but not 5
print(string[5:8])
print(string[:8])
print(string[:-3])
# print([len(string)-3])  [11] is printed as 14-3=11
print(string[0:len(string)-3]) #python interpreter take it as by default when wriring
# string[:-3] or string[0:-3]               {NEGATIVE SLICING}
print(string[-1:-3]) #this prints nothing len(string)-1=13 and len(string)-3=11
# so,there is no sense of 13:11
print(string[-3:-1])# starts from index 11(starting from 0) and goes upto 12th index


# It will not change the existing string rather will create new string so previous 
# string will not be changed {STRINGS ARE IMMUTABLE}
# String methods operate on a existing string and create a new string

print(string.upper())
print(string.lower())


# exclamatory mark at the end of string will only get striped off not the ones 
# present at the head or starting
name='**Ankita*****'
print(name.rstrip("*"))

#Repalce method used to replace an existing string with other string
b="Ankita Is Hardworking Person"
print(b.replace("Ankita","Carry"))

# Split method splits the given string (there should be spaces in b/w)
print(b.split(" "))

# Capitalize method converts one letter of string in upper case
blogheading="introduction to python"
print(blogheading.capitalize())
print(b.capitalize())

name2="Ankita Ankita is is  Ankita"
print(name2.count("Ankita"))
                                                    #  2/1/2025
#endswith method check whether string is ending with 
# given value or not
print(name2.endswith("+"))
string="Ankita is a girl"
print(string.endswith("a",7,11)) # this will check whether the substring between 
# index 7 and 11("is a") ending with a or not         return false
print(string.endswith("a",0,15))
print(string.endswith("l",0,16))


str_1="He's alsoo a good man . he is is hardworking"
print(str_1.find('he'))
print(len(str_1))

print(str_1.index('good'))
# print(str_1.index('Alsooo'))  ValueError: substring not found

str_1="He's alsoo a good man . he is is hardworking"
print(str_1.isalnum())
str2='Heisagoodboyhisageis18'
print(str2.isalnum())  #return true{ whole string should combined with no spaces in b/w}

print(str2.isalpha())
str3="heysiriowareyou"
print(str3.isalpha())
print(str3.replace("Heysirihowareyou","Heysirihowareyou1800"))
str_name='ankitasaini20062803'
print(str_name.isalpha())

print(str3.islower())

name1='Ankita\n'
print(str3.isprintable())
print(name1.isprintable())

space="   "
print(space.isspace())

print(str_1.title())
print(str_1.istitle())

str_1="He's alsoo a good man . he is is hardworking"
print(str_1.swapcase())   #convert lower case to upper case and vice-versa





