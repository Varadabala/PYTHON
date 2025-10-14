#Write a program that checks if a user-input string/number is a palindrome. 
# Do it using both string slicing and once without.

data = input("Enter a number or string : ")

if data == data[::-1]:
    print("Palindrome")
else:
    print("not palindrome")  
