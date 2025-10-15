n = int(input("Enter a number : "))

i = 1
while i <= n:
    # print spaces
    print(" " * (n - i), end="")

    # print ascending numbers
    j = 1
    while j <= i:
        print(j, end="")
        j += 1

    j = i - 1
    while j >= 1:
        print(j, end="")
        j -= 1    

    print()   # new line
    i += 1


#second method using for loop

for i in range(1, n + 1):
    # Print spaces
    for j in range(n - i):
        print(" ", end="")
    
    # Print increasing numbers
    for j in range(1, i + 1):
        print(j, end="")
    
    # Print decreasing numbers
    for j in range(i - 1, 0, -1):
        print(j, end="")
    
    print()

    
"""
Enter a number: 5
    1
   121
  12321
 1234321
123454321
"""