#Use //, % operators to break down a 4-digit number into its individual digits.
n = int(input("Enter a number : "))

thousand = n // 1000
hunderd = (n // 100) %10
tens = (n //10) %10
ones = n%10

print("Digits\n")

print("Thousands = ",thousand)
print("Hundreds = ",hunderd)
print("Tens = ",tens)
print("Ones = ",ones)


