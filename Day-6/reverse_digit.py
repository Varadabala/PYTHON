#4.	Write a function that reverses the positions of all digits and punctuation marks in a string,
#  but keeps the original position of all letters. 
# The letters should remain in their original order. Example: "A1b.2c!" --> "A!b2c.1".
def reverse_digits_punct(s):
    
    specials = []
    for ch in s:
        if not (('a' <= ch <= 'z') or ('A' <= ch <= 'Z')):
            specials.append(ch)


    specials = specials[::-1]

  
    result = []
    index = 0
    for ch in s:
        if not (('a' <= ch <= 'z') or ('A' <= ch <= 'Z')):
            result.append(specials[index])
            index += 1
        else:
            result.append(ch)

    return ''.join(result)


print(reverse_digits_punct("A1124b.2c!?^*"))  

'''
output
A*^?!b2.c4211
'''


