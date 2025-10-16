#1. Create a multiplication table till a number(entered by user) upto 10 using for loop and range.

n = int(input("Enter the number of a table : "))
a = int(input("Enter the end number : "))

for i in range(1,a+1):
    print(f"{n} x {i} = ",n*i)