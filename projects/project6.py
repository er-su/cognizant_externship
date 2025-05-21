# Calculator with exception handling

# This function prints the home menu and asks the user for their choice
def get_choice() -> int:
    while(True):
        print(
            "1: Addition\n" \
            "2. Subtraction\n" \
            "3. Multiplication\n" \
            "4. Division\n" \
            "5. Exit"
        )
        try: 
            val = int(input("Choose an option: "))
        except ValueError:
            print("Please enter a number!")
            continue
        else:
            return val
            

# Asks for two numbers and adds them together
def addition():
    while(True):
        try:
            n1 = float(input("Please enter the first number: "))
            n2 = float(input("Please enter the second number: "))
        except ValueError:
            print("Invalid number! Try again please")
            continue
        else:
            print(f"The sum of {n1} and {n2} is {n1 + n2}")
            break

# Asks for two numbers and subtracts them
def subtraction():
    while(True):
        try:
            n1 = float(input("Please enter the first number: "))
            n2 = float(input("Please enter the second number: "))
        except ValueError:
            print("Invalid number! Try again please")
            continue
        else:
            print(f"The difference of {n1} and {n2} is {n1 - n2}")
            break

# Asks for two numbers and multiplies them
def multiplication():
    while(True):
        try:
            n1 = float(input("Please enter the first number: "))
            n2 = float(input("Please enter the second number: "))
        except ValueError:
            print("Invalid number! Try again please")
            continue
        else:
            print(f"The product of {n1} and {n2} is {n1 * n2}")
            break
    
# Asks for two numbers and divides them
def division():
    while(True):
        try:
            n1 = float(input("Please enter the first number: "))
            n2 = float(input("Please enter the second number: "))
            val = n1 / n2
        except ValueError:
            print("Invalid number! Try again please")
            continue
        except ZeroDivisionError:
            print("Cannot divide by zero! Try again")
            continue
        else:
            print(f"The quotient of {n1} and {n2} is {val}")
            break

while(True):
    choice = get_choice()
    match choice:
        case 1:
            addition()
            continue
        case 2:
            subtraction()
            continue
        case 3:
            multiplication()
            continue
        case 4:
            division()
            continue
        case 5:
            print("Goodbye!")
            break
        case _:
            print("Not a valid choice! Please try again")
            continue