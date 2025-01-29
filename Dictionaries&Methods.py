'''
Dictiobaries in python are the key-value pairs separated by commas and enclosed
within curly brackets
'''
data={'Name':'Ankita Saini','Age':18,'Course':'BTECH CSE','Semester':'Fourth'}
print(type(data),data)

''' ACCESSING  Values in dictionaries'''
print(data['Name'])
print(data['Semester'])
print(data.get('Course'))
#  print(data['class']) key error bec key of name class is not present
print(data.get('class'))  #here error doesnot occur...NONE is printed

''' ACCESSING MULTIPLE VALUES'''
print(data.values())

''' ACCESSING MULTIPLE KEYS'''
print(data.keys())

''' ACCESSING KEY- VALUES PAIRS'''
print(data.items())

# if 'Semester' in data:
#     print(data['semester'])
#     print("Yes")
# else:
#     print("No")

if 'Name' in data:
    print(data.get('name'))
    print("Yes")

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
info.update({'age':20})
info.update({'DOB':2001})
info.update(data)
print(info)

info = {'name':'Karan', 'age':19, 'eligible':True}
info.clear()       #retuens an empty dictionary
print(info)  

info = {'name':'Karan', 'age':19, 'eligible':True}
info.pop('eligible')
print(info)

info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
info.popitem()
print(info)

info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info['age']
print(info)

info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info
# print(info)