# 1) append                                  8/1/2025
list=[2,4,3,1,1,1,6,4,19]
print(list)
list.append(32)
print(list)

# 2) sort
list.sort() 
print(list)
'''
list.sort() ->this will sort the list
print(list) -> this will print the list after sorting

print(list.sort()) -> this will return none because it is not returning 
anything
'''
# 3) index ->this will give the index at which given value is present
print(list.index(4)) 

# 4) Conactinating the list
list_02=[100,900,300]
Merge=list+list_02
print(Merge)

# 5) reverse
list_02.reverse()
print(list_02)
list.reverse()
print(list)

# 6) count
print(list.count(1))
print(list.count(4))
print(list.count(5))

# 7)extend
colors=['Red','Orange','Green']
numbers=[10,20,30,40,50]
colors.extend(numbers)
print(colors)

# 8) insert
colors.insert(1,'Baby Pink')
print(colors)

# 9)copy
Temp_list=colors.copy()
print(Temp_list)