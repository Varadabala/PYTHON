"""#Function with arguments and with return type

def simple_interest(p, t, r):
    return (p * t * r) / 100

p = float(input("Enter principal Amount: "))
t = float(input("Enter time: "))
r = float(input("Enter rate: "))

Interest = simple_interest(p, t, r)
print("Simple Interest =",Interest)

#Function with arguments and without return type

def simple_interest(p, t, r):
    SI = (p * t * r) / 100
    print("Simple Interest =",SI)

p = float(input("Enter principal Amount: "))
t = float(input("Enter time: "))
r = float(input("Enter rate: "))

simple_interest(p, t, r)
#Function without arguments and with return type
def simple_interest():
    p = float(input("Enter principal Amount: "))
    t = float(input("Enter time: "))
    r = float(input("Enter rate: "))
    SI = (p * t * r) / 100
    return SI

result = simple_interest()
print("Simple Interest",result)"""


#Function without arguments and without return type

def simple_interest():
    p = float(input("Enter principal Amount: "))
    t = float(input("Enter time: "))
    r = float(input("Enter rate: "))
    SI = (p * t * r) / 100
    print("Simple Interest =",SI)

simple_interest()