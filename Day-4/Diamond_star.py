n = int(input("Enter a number: "))

# Upper part
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# Lower part
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))


# Another form using while loop

# Upper half
i = 1
while i <= n:
    print(" " * (n - i) + "*" * (2 * i - 1))
    i += 1

# Lower half
i = n - 1
while i >= 1:
    print(" " * (n - i) + "*" * (2 * i - 1))
    i -= 1

    """
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
    """
