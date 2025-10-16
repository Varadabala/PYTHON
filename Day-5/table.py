#1. Create a multiplication table till a number(entered by user) upto 10 using for loop and range.

n = int(input("Enter the number of a table : "))
a = int(input("Enter the end number : "))

for i in range(1,a+1):

    print(f"{n} x {i} = ",n*i)


""""
output 
Enter the number of a table : 5
Enter the end number : 10
5 x 1 =  5
5 x 2 =  10
5 x 3 =  15
5 x 4 =  20
5 x 5 =  25
5 x 6 =  30
5 x 7 =  35
5 x 8 =  40
5 x 9 =  45
5 x 10 =  50

"""
