"""
1. Take a number as input from user. Ex-5 then output should be
1
12
123
1234
12345

"""

num = int(input("Enter a number : "))

for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,end = " ")
    print("")    
