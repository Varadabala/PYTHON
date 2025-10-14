#2. Create a dictionary where keys are numbers from 1 to 5 and values are their factorial. Use a for loop.

n = int(input("Enter the number : "))

dict = {}

for i in range(1,n+1):
    fact = 1
    for j in range(1,i+1):
        fact = fact *j
    dict[i] = fact    
print(dict)

#output -- Enter the number : 5
#{1: 1, 2: 2, 3: 6, 4: 24, 5: 120}