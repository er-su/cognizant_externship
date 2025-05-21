# About Parameters of Functions

# Task 1 - Writing Functions
def greet_user(name: str):
    print(f"Hello, {name}. Welcome aboard.")

def add_numbers(a, b):
    print(f"The sum of {a} and {b} is {a+b}")

greet_user("John")
add_numbers(5, 10)

# Task 2 - Using Default Parameters
def describe_pet(pet_name: str, animal_type: str="dog"):
    print(f"I have a {animal_type} named {pet_name}")

describe_pet("Buddy")
describe_pet("Whiskers", "cat")

# Task 3 - Fonctions with variable Arguments
def make_sandwich(*args: str):
    print("Making a sandwhich with the following ingredients: ")
    for arg in args:
        print(f"- {arg}", end=" ")
    print("")

make_sandwich("Lettuce", "Tomato", "Cheese")

# Task 4 - Understanding Recusion
def factorial(n: int) -> int:
    if n == 1:
        return 1
    
    return n * factorial(n - 1)

n = 5
print(f"Factorial of {n} is {factorial(n)}")

def fibonacci(n: int) -> int:
    if n == 1:
        return 0
    elif n == 2:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)

print(f"The {n-1}th fibonacci number is {fibonacci(n)}")