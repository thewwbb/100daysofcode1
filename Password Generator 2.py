import string
import random

lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation
password = []

print("Welcome to my password generator application!")
print("How many lowercase letters would you like?")
number_of_lowercase_letters = int(input())
print("How many uppercase letters would you like?")
number_of_uppercase_letters = int(input())
print("How many numbers would you like?")
number_of_numbers = int(input())
print("How many symbols would you like?")
number_of_symbols = int(input())

for _ in range(number_of_lowercase_letters):
    password.append(random.choice(string.ascii_lowercase))
for _ in range(number_of_uppercase_letters):
    password.append(random.choice(string.ascii_uppercase))
for _ in range(number_of_numbers):
    password.append(random.choice(numbers))
for _ in range(number_of_symbols):
    password.append(random.choice(symbols))

password_string = "GOODLUCKIKNOWYOURPASSWORD".join(password)

print(f"Your password is {password_string}")

