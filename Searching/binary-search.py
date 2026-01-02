#How to find a binary search using python

"""
Algorithm: Binary Search

Start
Input sorted array A and search key  k
Set low = 0, high = n -1 
Compute mid = (low + high) / 2 and compare with k
Repeat till found or low > high, else print Not Found
"""


#without using funtion and no return type
arr = [10,20,30,40,50,60,70]
key = int(input("Enter a number to find: "))

flag = 0
index = 0
l = len(arr)

low = 0
high = l - 1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == key:
        flag = 1
        index = mid
        break
    elif key < arr[mid]:
        high = mid - 1
    else:
        low = mid + 1

if flag == 1:
    print("Element found at index", index)
else:
    print("Element not found")



#with Function and return type

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif key < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1


# Main program
arr = [10, 20, 30, 40, 50, 60, 70]
key = int(input("Enter element to search: "))

result = binary_search(arr, key)

if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")



"""
o/p :
Enter a number to find: 20
Element found at index 1

Enter a number to find: 90
Element not found
"""