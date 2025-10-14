#Write a program that checks if a user-input string/number is a palindrome. 
# Do it using both string slicing and once without.

data = input("Enter a number or string : ")

reverse = ""

for ch in data :
    reverse = ch + reverse


if data == reverse:
    print("Palindrome")
else:
    print("NOt a palindrome")    
