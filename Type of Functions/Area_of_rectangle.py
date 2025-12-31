"""#Function with arguments and with return type
def area(l,b):
    return l *b


l = float(input("Enter Length :"))
b = float(input("Enter Breadth "))

s = area(l,b)
print(s)


#Function with arguments and no return type
def area(l,b):
    area = l*b
    print(f"Area of rectangle is",area)


l = float(input("Enter Length :"))
b = float(input("Enter Breadth :"))

area(l,b)

#Function without arguments and with return type
def area():
    l = float(input("Enter Length :"))
    b = float(input("Enter Breadth :"))

    return l*b

Area = area()
print(Area)
"""
#Function without arguments and no return type

def area():
    l = float(input("Enter Length :"))
    b = float(input("Enter Breadth :"))

    area = l*b
    print(f"Area of rectangle is",area)

area()
