#WAP to find the character in a string and remove the character 
s = input("Enter a string : ")
ch = input("Enter a char to remove : ")

output = ""
i = 0
length = len(s)
while(i<length):
    if s[i] == ch:
        output = s[:i] + s[i+1:]
        break
    i = i+1

print(f"character found at index {i}")        
print(f"Output is : {output}")

"""
Enter a string : hello
Enter a char to remove : l
character found at index 2
Output is : helo

"""