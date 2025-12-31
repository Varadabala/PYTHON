"""#Function with arguments and with return type

def Even_odd(n):
    if (n % 2) == 0:
        return "Even"
    else:
        return "odd"
    
num = int(input("Enter a number : "))
k = Even_odd(num)
print(k)    

#Function with arguments and no return type

def Even_odd(n):
    if (n % 2) == 0:
        print(f"{n} is Even Number")
    else:
        print(f"{n} is Odd Number")
    
num = int(input("Enter a number : "))
Even_odd(num)

#Function with out arguments and with return type
def Even_odd():
    n = int(input("Enter a number : "))
    if (n % 2) == 0:
        return "Even"
    else:
        return "odd"

result = Even_odd()
print(result)
"""
#Function with out arguments and without return type
def Even_odd():
    n = int(input("Enter a number : "))
    if (n % 2) == 0:
        print(f"{n} is Even Number")
    else:
        print(f"{n} is Odd Number")

Even_odd()