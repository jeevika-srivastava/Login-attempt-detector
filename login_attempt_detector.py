attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input("Enter password: ")

    if password == "admin123":
        print("Login successful")
        break
    else:
        attempts += 1
        print("Wrong password")

if attempts == max_attempts:
    print("Too many failed attempts. Access blocked.")