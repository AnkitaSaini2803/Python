#3-3-2025 
# Given an array ‘arr’ of size ‘n’ find the largest element in the array.
arr=[19,78,34,2,1,90,12,3,444,5,88,999]
def Largest_Element(arr):
    for i in arr:
        return max(arr)
print(Largest_Element(arr))

# 2 .Bestt
def Largest(arr):
    max=arr[0]
    for i in arr[1:]:
        if i>max:
            max=i
    return max
print(Largest(arr))

#3.
arr.sort()
print(arr[-1])

#4.
def Large(arr):
    max_element=0
    for i in arr:
        max_element=max(max_element,i) 
    return max_element
print(Large(arr))