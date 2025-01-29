'''Write a python program to translate a message     14/1/2025
into secret code language. Use the rules below to translate
 normal English into secret code language

Coding:
if the word contains atleast 3 characters, remove the first letter
 and append it at the end
 now append three random characters at the starting and the end
else:
  simply reverse the string

Decoding:
if the word contains less than 3 characters, reverse it
else:
  remove 3 random characters from start and end. Now remove the
    last letter and append it to the beginning
Your program should ask whether you want to code or decode
'''

string=input("Enter The String :")
if(len(string)>=3):
    # string=len(string)-string[0]   ERROR DONO AAPS MEIN COMPATIBLE NAHI HAIN
    string=string[1:]+string[0]
    print(string)
    random=input("Enter any 3 random characters ")
    if(len(random)==3):
         string=string+random
         print(string)
         string=random+string
         print(string)
    else:
         print("The values you enetered are lesser than or greater than 3")

else:
     string=string[0::-1]
     print(string)
# print(string.reverse()) There is no built-in function to reverse a String in Python    

    
   