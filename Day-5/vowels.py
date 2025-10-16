
#2. Write a function that uses a for loop to count vowels in a string. Demonstrate local variable scope.

#without function

word = input("Enter a string : ")
count = 0
vowels = "aeiouAEIOU"
for i in word :
    if i in vowels:
        count += 1
print("Count of vowels = ",count)     


#with Function

def vowels_count(item):
    count = 0
    vowels1= "aeiouAEIOU"
    for i in item :
        if i in vowels1:
            count += 1
    return count

item = input("Enter a string : ")
print("Vowels-count = ",vowels_count(item))
