#Function with arguments and with return type
def prime_check(n):
    flag = 0

    if n <= 1:
        flag = 1
    else:
        for i in range(2, n):
            if n % i == 0:
                flag = 1
                break

    if flag == 0:
        return "Prime"
    else:
        return "Not Prime"

num = int(input("Enter a number: "))
print(prime_check(num))


#Function with arguments and without return type
def prime_check(n):
    flag = 0

    if n <= 1:
        flag = 1
    else:
        for i in range(2, n):
            if n % i == 0:
                flag = 1
                break

    if flag == 0:
        print(f"{n} is a Prime Number")
    else:
        print(f"{n} is not a Prime Number")

num = int(input("Enter a number: "))
prime_check(num)
#Function without arguments and with return type

def prime_check():
    n = int(input("Enter a number: "))
    flag = 0

    if n <= 1:
        flag = 1
    else:
        for i in range(2, n):
            if n % i == 0:
                flag = 1
                break

    if flag == 0:
        return "Prime"
    else:
        return "Not Prime"


print(prime_check())
#Function without arguments and without return type
def prime_check():
    n = int(input("Enter a number: "))
    flag = 0

    if n <= 1:
        flag = 1
    else:
        for i in range(2, n):
            if n % i == 0:
                flag = 1
                break

    if flag == 0:
        print(f"{n} is a Prime Number")
    else:
        print(f"{n} is not a Prime Number")


prime_check()