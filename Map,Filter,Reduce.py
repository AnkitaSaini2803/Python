''' 16/1/2025
Without using map function
'''
l=[1,2,4,6,4,3]
def cube(x):
    return x*x*x
l1=[]          
for i in l:
    l1.append(cube(i))
    # print(l1)
print(l1)

'''Using map function'''
l=[1,2,4,6,4,3]
for i in l:
    l1=list(map(cube,l))
print(l1)

'''Using map with lambda'''
list0=[1,5,4,6,2,3]
for i in list0:
    list1=list(map(lambda x:x*x*x,list0))
print(list1)

'''Filter Function'''
lis=[5,3,2,4,1,6]
def filter_function(a):
    return a>2
new_lis=list(filter(filter_function,lis)) # function will return a boolean 
# value and is applied to each element in the iterable argument.
print(new_lis) 

'''Filter with lambda
new_lis=list(filter(lambda a:a>2,lis))
print(new_lis) 
'''

'''Reduce function'''
from functools import reduce
numbers=[7,8,5,4,2,1]
sum=reduce(lambda x,y:x+y,numbers)
print(sum)