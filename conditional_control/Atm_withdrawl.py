balance = 5000
amount = int(input("Enter withdrawal amount: "))

if amount <= balance:
    if amount % 100 == 0:
        print("Collect your cash")
    else:
        print("Enter amount in multiples of 100")
else:
    print("Insufficient balance")

