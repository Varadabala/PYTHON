#To remove the vowels in a string
s = input("Enter a string : ")
l = []

for i in s.lower():
    if i not in ('a','e','i','o','u'):
        l.append(i)

print(l)                #['h', 'l', 'l', ' ', 'h', 'w', ' ', 'r', ' ']
print("".join(l))       #hll hw r

"""
O/P:

Enter a string : HELLO HOW ARE U
['h', 'l', 'l', ' ', 'h', 'w', ' ', 'r', ' ']
hll hw r 
"""

#WE  done this using regular expression

import re

print(re.sub("[aeiou]","",input("enter a string : ")))