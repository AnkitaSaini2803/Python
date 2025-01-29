# 31/12/2024
print('Radhe Radhe')
Name="Ji"
print("Hello"+Name)

# Single Line Strings
# print("Hey,"I want to eat Maggie",") Double quotes can be enclosed within single quotes
print(' Hey,"I want to eat Maggie" ')

# Multi Line strings (USING SINGLE TRIPLE QUOTES)
'''
print("Hey, My name is Ankita
      I am good
      what about you
      I just wanted to say 
      that I'm Hungry
      ")
 '''

Nameofstring='''Hey, My name is Ankita
      I am good
      what about you
      I just wanted to say 
      that I'm Hungry'''
print("The string is: ", Nameofstring)

# Accessing characters of single line strings
print(len(Name))
print(Name[0])
print(Name[1])
# print(Name[2])       Here comes index error(this index is not available)

# Accessing characters of Multi line strings using for loop
# for character in name:
# print(character)

for character in Nameofstring:
    print(character)