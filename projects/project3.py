# Password Strength Checker
password = input("Input a password: ")

strong = True
if not any(char.isdigit() for char in password):
    print("Must contain a digit!")
    strong = False

if not any(char.isupper() for char in password):
    print("Must contain an uppercase letter!")
    strong = False

if not any(char.islower() for char in password):
    print("Must contain lowercase letter!")
    strong = False

if not any(not char.isalnum() for char in password):
    print("Must contain a special character!")
    strong = False

if strong:
    print("Your password is strong!")