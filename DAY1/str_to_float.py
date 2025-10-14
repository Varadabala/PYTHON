#. Take two numbers and a string (e.g., "5.7") from user input. 
# Convert the string to a float, perform addition with the first number, and multiplication with the second. 
# Print all data types involved.


num1 = int(input("Enter the number1 : "))
num2 = int(input("Enter the number2 : "))
string = input("Enter the string : ")

float_num = float(string)

add = num1 + float_num
mul = num2*float_num

print("ADDITION = ",add)
print("MULTIPLY = ",mul)
print(type(num1),type(num2),type(float_num),type(add),type(mul))



