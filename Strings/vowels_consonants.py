#To find the count of vowels and consonants in a string
s = input("Enter a string : ")
count1 = 0
count2 = 0

for i in s:
    if i in('a','e','i','o','u'):
        count1 = count1+1
    else:
        count2 = count2+1

print(f"Vowels count = {count1}")
print(f"Consonants count = {count2}")          

"""
o/p:

Enter a string : you are the creatoe of your destiny
Vowels count = 14
Consonants count = 21
"""