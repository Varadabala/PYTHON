#To check a given string is palindrome or not
s = input("Enter a string : ")

empty = ""

for i in s:
    empty = i + empty

print(empty) 

if s == empty:
    print("Palindrome")
else:
    print("Not a palindrome")  

"""
o/p:
Enter a string : malayalam
Palindrome

Enter a string : check
Not a palindrome
"""
      