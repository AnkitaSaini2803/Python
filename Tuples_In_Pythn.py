#  9/1/2025

countries=('India','germany','russia','thailand','america','US')
print(type(countries),countries)

'''
When keeping only one element inside a tuple

country=('India')
print(type(country),country)
tuple=(1)
print(type(tuple),tuple)

'''
country=('India',)
print(type(country),country)

tuple=(1,)
print(type(tuple),tuple)

# CHANGING TUPLE INTO LIST(MODIFYING )

countries=('India','germany','russia','thailand','america','US')
temp_list=list(countries)
print(type(temp_list),temp_list)
print(type(countries),countries)
print(temp_list[0])
print(countries[1])
temp_list.append('London')
print(temp_list)

temp_list.reverse()
print(temp_list)
temp_list.pop(4)
print(temp_list)

# Concatenating two tuples and storing them in third tuple named merge 
countries=('India','germany','russia','thailand','america','US')
num=(1,2,10,20,'green',True)
merge=countries+num
print(type(merge),merge)

# TUPLES METHOD            1) COUNT
print(countries.count('India'))
print(countries.count(''))    # 0 aayega
# print(countries.count())   TYPE ERROR WILL OCCUR
 
# 2) INDEX                   syntax:              tuple.index(element, start, end)
print(countries.index('thailand'))
num1=(1,2,10,1,1,1,3,20,'green',True)
print(num1.index(1,3,7))   #it will give the first occurence of 1 between index 3 to 7
