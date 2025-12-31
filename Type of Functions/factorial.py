"""#function with arguments and with return type
def factorial(a):
    fact = 1
    for i in range(1,a+1):
        fact = fact*i
    return fact


n = int(input("Enter a number : "))
k = factorial(n)
print(f"Factorial of a {n} is",k)

#function with argumentss and no return type

def factorial(a):
    fact = 1
    for i in range(1,a+1):
        fact = fact*i
    print(f"Factorial of a {n} is",fact)


n = int(input("Enter a number : "))
factorial(n)

#function without arguments and with return type

def factorial():
    n = int(input("Enter a number: "))
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact

result = factorial()
print("Factorial =", result)
"""
#Funtion without arguments and without return type

def factorial():
    n = int(input("Enter a number: "))
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    print("Factorial =", fact)

factorial()
