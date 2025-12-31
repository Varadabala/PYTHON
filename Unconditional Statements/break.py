#Break -- > it is a unconditional control statements it exits out of the program when it mets the condition

#Program: Stop loop when number is 5
n = int(input("Enter a number : "))

for i in range(1, n):
    if i == 5:
        break
    print(i, end = " ")
