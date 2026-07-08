import string

alphabet = string.ascii_lowercase

print("Welcome to my encrypt/decrypt program!")

message = input("Enter your message: ")
shift = int(input("Enter shift amount: "))

encrypted_message = ""

for letter in message:
    print(letter)