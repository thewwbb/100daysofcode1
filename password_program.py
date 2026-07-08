secretPassword = "0000"
password_list = []

for password_attempt in range(4):
    print("Enter your password.")
    typedPassword = input()

    if typedPassword == "12345":
        print("That password is one that an idiot puts on their luggage.")

    if typedPassword == secretPassword:
        print("Access granted")
        password_list.append(typedPassword)
        break
    else:
        print("Access denied")

print(password_list)