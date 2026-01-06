#Adding duplicates to the sting
s = input("Enter a string : ")
l = []

for i in s:
    l.append(i*2)
print(l)
print("".join(l))   

"""
o/p:
Enter a string : abcd
['aa', 'bb', 'cc', 'dd']
aabbccdd
"""