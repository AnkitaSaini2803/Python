# SETS            10/1/2025
s={1,3,4,2,2,8,4,1,1}
print(type(s),s)
info={True,'hey',6,'hey',4,1,6}
print(type(info),info)
# set={''}
# print(type(set),set)
# sett={}
# print(type(sett),sett)         #dict

'''
#  Create an EMPTY set
# '''
harry = set()
print(type(harry))

''' items of sets are accessed using for loops
'''
for i in info:
    print(i)
for j in s:
    print(j)

# Sets Methods
# Union() and update()
cities_1={'Berlin','Delhi','tokya','Madrid'}
cities_2={'tokya','sebul','kabul','Madrid'}
cities_3=cities_1.union(cities_2)
print(cities_3)
# cities_4=cities_2.union(cities_1)
# print(cities_4)

cities_2.update(cities_1)
print(cities_2)
# cities_1.update(cities_2)
# print(cities_1)

# intersection() and intersection_update()
cities_3=cities_1.intersection(cities_2)
print(cities_3)
cities_1.intersection_update(cities_2)
print(cities_1)

# 11/1/2025
# symmetric_difference() and symmetric_difference_update()
cities_1={'Berlin','Delhi','tokya','Madrid'}
cities_2={'tokya','sebul','kabul','Madrid'}
cities_3=cities_1.symmetric_difference(cities_2)
print(cities_3)

cities_2.symmetric_difference_update(cities_1)
print(cities_2)

'''
SETS METHOD IN PYTHON
'''
# 1) isdisjoint()
basket1={'flowers','fruits','colors',True,'string','tuple','list','set'}
basket3={'red','pink','jaal','jaipur'}
basket2={'flowers',True,'orange','mango'}
basket4={'flowers','fruits','colors',True,'string'}
print(basket1.isdisjoint(basket3))   #true bec. no element is common in both sets
print(basket1.isdisjoint(basket2)) 

# 2) issuperset()
print(basket2.issuperset(basket1))
print(basket4.issuperset(basket1))
print(basket1.issuperset(basket4))

# 3) issubset()
print(basket4.issubset(basket1))

# 4) add() and update()
basket2.add('Jalandhar')
print(basket2)

basket2.update(basket3)
print(basket2)

# 5) remove() or discard()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities.remove("Tokyo")
# print(cities)

# cities.discard('Tokya')
# print(cities)

cities.discard('tokya')
print(cities)         #{'Madrid', 'Berlin', 'Delhi', 'Tokyo'} 

'''
cities.remove("tokyo")
print(cities)        #KeyError: 'tokyo'

cities.remove("Rajasthan")
print(cities)            #KeyError
'''

'''
6)  pop():This method removes the last item of the set 
 but the catch is that we don’t know which item gets popped
  as sets are unordered
'''

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item)

#7)del is not a method, rather it is a keyword which deletes the set entirely.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities
# print(cities)

'''
NameError: name 'cities' is not defined We get an error because our
entire set has been deleted and there is no variable called cities
which contains a set.
What if we don’t want to delete the entire set, we just want to delete
all items within that set?

'''
# 8)clear()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)      #set()


# You can also check if an item exists in the set or not
info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")