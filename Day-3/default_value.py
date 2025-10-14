#4. Simulate a "default value" for a key without using .get().

d = {"a": 1, "b": 2, "c": 3,"d" : 4}
key = input("Enter key: ")

if key in d:
    value = d[key]
else:
    value = 0  # default value

print("Value:", value)


"""
output

Enter key: a
Value: 1

Enter key: f
Value: 0
"""