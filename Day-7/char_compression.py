#1. Character Compression: Implement a function that takes a string and compresses it by replacing consecutive repeating characters with the character followed by its count. 
# If the compressed string is not shorter than the original, return the original string. Example: "aaabbcca" --> "a3b2c2a1".

'''s = input("Enter a string: ")
compressed = ""
count = 1

for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        count += 1
    else:
        compressed += s[i - 1] + str(count)
        count = 1
compressed += s[-1] + str(count)

if len(compressed) < len(s):
    print(compressed)
else:
    print(s)
    
'''

a=input("Enter a string : ")
b=""
c=""
for i in a:
    if b == "":
        b+=i
    elif i == b[-1]:
        b+=i
    else:
        c+=b[-1]+str(len(b))
        b=i
c += b[-1] + str(len(b))        
print(c)

'''
output
Enter a string : aaadddhhh
a3d3h3
'''
    
   






