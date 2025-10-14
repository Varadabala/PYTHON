#3. Demonstrate list aliasing and cloning. 
# Show that modifying a clone doesn't affect the original, but modifying an alias does.

original = [1,2,3,4]

alias = original

clone = original[:]

alias.append(5)

print("After modifing alias")
print(alias)
print(original)
print(clone)

clone.append(20)
print("\nAfter modifing clone")
print(alias)
print(original)
print(clone)

""" output -- 
After modifing alias
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
[1, 2, 3, 4]

After modifing clone
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 20]
"""