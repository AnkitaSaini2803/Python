#Day1 in learning python language                  30/12/2024
# Use of print function
print("Hello World",5,"Python first class")
print("Python First Program")
# This sigle line comment is there to explain multi-line comment
# shortcut= ctrl + forwardslash(/)
'''
print(20*15)
print(72+43)
print(45-30)
print(200/5)
'''

print(5.5//3)    # Floor Division OPERATOR in python(It will round off the quotient value to nearest integer value)
#when dividing 5 by 3 we'll get 1 BUT when dividing 5.5 by 3 we'll get 1.0
print(5.5 % 3)   # Modulus operator will give the remainder value
#This will give us 2.5 as result(remainder)
print(8**5)    # Exponential operator = 8*8*8*8*8



#Escape Sequence Character
print("I am a \"Ambivert\" girl and\nalso my teammates are introvert")

'''
Parameters of print statement
1) separator
2) end
3) file
4)object
'''

# Separator = to separate multiple values
print('Hii',7,9,sep="#")
print("Hii",7,9,sep="~")

# Specify with what you want to end the line
print('''Ankita''',9,0,end="007\n")
print("Ji")

#String datatype
str='Coding Ninjas'
print(str[0])                      #Accessing character in a string
print(str+' Academy')              #Concatenating  the string
print(len(str))                   #Finding length of string
print(str[7:])               #Prints the substring starting from 7th index
print(str[0:6])              #Prints the substring starting from index 0 and ending at index 5

#24/1/2025
s='''Multi-Line STATEMENTS'''
print(s)
r='''these are
Multi-Line STATEMENTS'''
print(r)

speech=("Good After Noon\nI hope you all are good\nso,today we gathered here forr some Special work\n")
print(speech)

list=[3,5,
      4,5,21,0]
print(list)

