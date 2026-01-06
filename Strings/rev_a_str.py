#Reverse a string 

#1st method
s = input("Enter a string : ")

empty = " "

for i in s:
    empty = i + empty

print(empty) 

#2nd method

T = input("Enter a string : ")
print(T[::-1])
