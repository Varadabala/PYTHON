"""
2. Take a number as input from user. Ex-5 then output should be
*****
****
***
**
*
"""  

n = int(input("Enter a number: "))

for i in range(n, 0,-1):
    for j in range(i):
        print("*", end=" ")
    print()

#second  way using for loop

for i in range(1, n + 1):
    print("*" * (n - i + 1))

# third way using while loop
i = n
while(i>=1):
    print("*" *i)
    i -= 1

   