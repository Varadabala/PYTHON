#WAP to print the word if the length is even

s = input("Enter a string : ")
for word in s.split():
    if len(word) % 2 == 0:
        print(word,end = " ")

"""
o/p :

Enter a string : all my students are awesome
my students 

Enter a string :  python is very smple
python is very 
"""        