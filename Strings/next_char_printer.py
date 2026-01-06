#WAPto find the next charcter of a charecter in a word
s =input("Enter a string : ")

for ch in s:
    print(ord(ch) + 1,end = " ")                  #here it will give the number of the character
    print(chr(ord(ch) + 1),end = " ")             #here it will give the character of a number by using {chr} function

"""
o/p : 
Enter a string : abc
98 b 99 c 100 d 

Enter a string : password
113 q 98 b 116 t 116 t 120 x 112 p 115 s 101 e
"""