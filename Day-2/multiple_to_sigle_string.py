#4. Convert a tuple of strings into a single string without using .join().
tup = ('python','is','fun')

empty = ""

for word  in tup:
    empty = empty + word + " "

print(tup)
print(empty)


#output -- python is fun