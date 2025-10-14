#3. Write a function that takes a list of words and returns a dictionary with the word as the key and its length as the value.

def func(words):
    dict = {}
    for i in words:
        dict[i] = len(i)
    return dict        

words = ["apple","banana","grapes","pineapple"]    

print(func(words))



#output : {'apple': 5, 'banana': 6, 'grapes': 6, 'pineapple': 9}