import random
import string

letters = string.ascii_letters

def generate_password(min_length, numbers=True, special_characters=True):
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    while len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char
        has_number = any(char.isdigit() for char in pwd)
        has_special = any(char in special for char in pwd)

    return pwd

min_length = int(input("Enter the minimum length: "))
has_number = input("Do you want numbers in your password? (y/n): ").lower() == "y"
has_special = input("Do you want special characters in your password? (y/n): ").lower() == "y"
pwd = generate_password(min_length, has_number, has_special)

print("The generated password is: ", pwd)
