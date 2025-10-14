#3. Simulate a simple login: Check if a username is not "admin" OR a password is "12345", print "Access Denied", else "Granted".


username = input("Enter a username : ")
password = input("Enter a password : ")

if(username == "Admin" and password == "12345"):
    print("Access Granted")
else:
    print("Access Denied")
