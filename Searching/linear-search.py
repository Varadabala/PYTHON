#How to write a linear search in python

"""
Algorithm: Linear Search

Start
Input array A and search key key
Compare key with each element of A sequentially
If a match is found, print Found and exit
Else, after full traversal, print Not Found and stop
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


"""
o/p:
Enter a number to find :50
Element found at index  4


Enter a number to find :100
Element not found
"""