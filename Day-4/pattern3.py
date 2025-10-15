n = int(input("Enter a number : "))

for i in range(1, n + 1):
    # Print spaces
    for j in range(n - i):
        print(" ", end="")
    
    # Print increasing numbers
    for j in range(1, i + 1):
        print(j, end="")

    print()    

    """
    Enter a number : 5
    1
   12
  123
 1234
12345
    """    