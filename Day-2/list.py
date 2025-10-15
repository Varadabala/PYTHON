# Create a list from user input, find duplicates, and return a set of those duplicates.

user =list(map(int,input("Enter a list of elements : ").split()))
a={}

for i in user:
    if i in  a:
        a[i]+=1
    else:
        a[i]=1
print(a)
b=list()
for j,k in a.items():
    if k>1:
        b.append(j)
print(set(b))

"""
output 

Enter a list of elements : 1 2 3 1 3 2
{1: 2, 2: 2, 3: 2}
{1, 2, 3}
"""



user_input = input("Enter list elements separated by spaces: ")
lst = user_input.split()

duplicates = set()   # to store duplicates
for i in lst:
    if lst.count(i) > 1:
        duplicates.add(i)

print("Original list:", lst)
print("Duplicates as sets : ",duplicates)
