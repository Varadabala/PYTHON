#WAP to check the given string is sorted or not

s = input("Enter a string : ")
l = list(s)
print(l)
sorted_list = l.copy()
sorted_list.sort()

print("Ordered" if l == sorted_list else "Unordered")

"""
o/p:

['a', 'c', 'r', 'd']
Unordered

['a', 'b', 'c', 'd', 'f']
Ordered
"""