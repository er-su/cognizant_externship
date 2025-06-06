# This function prints the home menu and asks the user for their choice
def get_choice() -> int:
    while(True):
        print("1: Calculate factorial\n" \
        "2. Find fibonacci\n" \
        "3. Draw a recursive fractal\n" \
        "4. Exit")

        num = int(input("Choose an option: "))
        if num > 0 and num < 6:
            return num
        else:
            print("Invalid selection")

# This function asks the user to input an integer greater than 0
def get_num() -> int:
    while(True):
        num = int(input("Select a number: "))
        if num > 0:
            return num
        else:
            print("Invalid selection")  

# This function calculates the factorial of n
def factorial(n: int) -> int:
    if n == 1:
        return 1
    
    return n * factorial(n - 1)

# This function finds the fibonacci number at position n where
# position 0 is 0 and position 1 is 1
def fibonacci(n: int) -> int:
    if n == 1:
        return 0
    elif n == 2:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)

def fractal():
    print("This has not been defined yet")

while(True):
    choice = get_choice()
    match choice:
        case 1:
            n = get_num()
            print(f"Factorial of {n} is {factorial(n)}")
        case 2:
            n = get_num()
            print(f"Fibonacci at position {n} is {fibonacci(n)}")
        case 3:
            fractal()
        case 4:
            break