
#1. Create a list from user input, find duplicates, and return a set of those duplicates.
#2. Given two lists, find the common elements without using set.intersection().

#4. Convert a tuple of strings into a single string without using .join().

list1 = input("Enter the elements of list1 : ").split()
list2 = input("Enter the elements of list2 : ").split()

common = []
for i in list1:
    if i in list2 and i not in common:
        common.append(i)

print(list1)
print(list2)
print(common)         