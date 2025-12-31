#check eligibility to vote

age = int(input("Enter age: "))
country = input("Enter country: ")

if age >= 18:
    if country == "India":
        print("Eligible to vote")
    else:
        print("Not eligible to vote")
else:
    print("Not eligible to vote")
