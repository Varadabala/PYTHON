#1. Create a multiplication table till a number(entered by user) upto 10 using for loop and range.

n = int(input("Enter the number of a table : "))
a = int(input("Enter the end number : "))

for j in range(1,n+1):
    for i in range(1,a+1):
        print(f"{j} x {i} = ",j*i)

""""
output 
Enter the number of a table : 4
Enter the end number : 5
1 x 1 =  1
1 x 2 =  2
1 x 3 =  3
1 x 4 =  4
1 x 5 =  5
2 x 1 =  2
2 x 2 =  4
2 x 3 =  6
2 x 4 =  8
2 x 5 =  10
3 x 1 =  3
3 x 2 =  6
3 x 3 =  9
3 x 4 =  12
3 x 5 =  15
4 x 1 =  4
4 x 2 =  8
4 x 3 =  12
4 x 4 =  16
4 x 5 =  20

"""

