#How to write a linear search in python

"""
Algorithm: Linear Search

Start from the first element of the list.
Compare the current element with the key.
If it matches, return the index (or position).
If not, move to the next element.
If the end is reached, element is not found.
"""



#Without using Funtion and no return type
arr = [10,20,30,40,50,60,70]
key = int(input("Enter a number to find :"))
flag = 0
index = 0
l = len(arr)

for i in range(l):
    if arr[i] == key:
        flag = 1
        index = i
        break

if(flag == 1):
    print("Element found at index ",index)
else:
    print("Element not found")        


#Linear searchusing Funtion with return type

def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


# Driver code
arr = [5, 8, 2, 9, 1, 7]
key = 9

result = linear_search(arr, key)

if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")



"""
o/p:
Enter a number to find :50
Element found at index  4


Enter a number to find :100
Element not found
"""
