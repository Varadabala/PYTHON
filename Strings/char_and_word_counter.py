s = input("Enter a string : ")
char_count = 0
word_count = 0
for ch in s:
    char_count = char_count + 1
    if ch == " ":
        word_count = word_count + 1 

print("Character Count = ",char_count)
print("Word Count = ",word_count + 1)