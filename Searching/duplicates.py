#Find the duplicate elements in the list

lst = [1, 2, 3, 1, 2, 4, 5, 3, 3]

duplicates = []

for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] == lst[j] and lst[i] not in duplicates:
            duplicates.append(lst[i])

print("Duplicate elements:", duplicates)

"""
o/p:
Duplicate elements: [1, 2, 3]
"""