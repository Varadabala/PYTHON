#2. Given two lists, find the common elements without using set.intersection().

list1 = input("Enter the elements of list1 : ").split()
list2 = input("Enter the elements of list2 : ").split()

common = []
for i in list1:
    if i in list2 and i not in common:
        common.append(i)

print(list1)
print(list2)
print(common)  
__________________________________________________________________

list1 = [1,2,3 ,4,5,6]
list2 = [1,2,3, 6,7,8 ,9]

common = []

for i in list1:
    for j in list2:
        if i == j:
            common.append(i)

print(list1)
print(list2)
print(common)
______________________________________________________________________
"""
output 

Enter the elements of list1 : 1 2 3 4 5
Enter the elements of list2 : 4 5 6 7 8
['1', '2', '3', '4', '5']
['4', '5', '6', '7', '8']
['4', '5']

"""
