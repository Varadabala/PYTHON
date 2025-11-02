##3.	Nested Vowel Extraction: Take a user input string. 
# Create a nested dictionary where the top-level keys are the vowels ('a', 'e', 'i', 'o', 'u') found in the string. 
# The value for each vowel key should be another dictionary containing the count of that vowel 
# and a list of all characters that immediately follow that vowel in the original string.


def nested_vowel_extraction(text):
    vowels = 'aeiou'
    result = {}

    for i in range(len(text)):
        ch = text[i].lower()
        if ch in vowels:
            if ch not in result:
                result[ch] = {'count': 0, 'next_chars': []}
            result[ch]['count'] += 1
            if i + 1 < len(text):
                result[ch]['next_chars'].append(text[i + 1])

    return result


print(nested_vowel_extraction("Thundersoft"))


'''
output
{'u': {'count': 1, 'next_chars': ['n']}, 'e': {'count': 1, 'next_chars': ['r']}, 'o': {'count': 1, 'next_chars': ['f']}}
'''