'''Given an array/list 'ARR' of integers and a position m.              5-3-2025 
You have to reverse the array after that position.    INTERVIEW PROBLEM
'''
def reverseArray(arr, m):
    result=[]
    # Write your code here.
    if m<=len(arr):
        result.extend(arr[0:m+1])
        new_arr=arr[m+1:]
        new_arr.reverse()
        result.extend(new_arr)
        return result
arr=[2,3,4,1,5,6,7]
print(reverseArray(arr,1))  
    

# Solution 2                                  125 ms runtime        7-3-2025
def reverse(array,M):
    l=array[0:M+1]
    k=array[M+1:]
    k=k[::-1]
    return l+k
array=[6,7,1,2,8,9,22,3,45,21]
print(reverse(array,4))


# Solution 3                                      127 ms runtime
def arr_rev(arr,n):
    arr[n+1:]=arr[n+1:] [::-1]
    return arr

arr=[6,3,66,2,1,8,0,9,4]
print(arr_rev(arr,2))