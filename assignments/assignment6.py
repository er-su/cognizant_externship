# Check your Knowledge on Errors

# Task 1 - Understanding Python Exceptions
try:
    user_in = int(input("Enter a number! "))
    print(f"100 divided by {user_in} is {100 / user_in}")

except ZeroDivisionError:
    print("Oops! You cannot divide by zero")

except ValueError:
    print("Please enter a valid number")

# Task 2 - Types of Exceptions
array = list(range(10))
try:
    val = array[100]
except IndexError:
    print("IndexError occured! List index out of range")

dic = {
    "a": 1,
    "b": 2,
    "c": 3
}
try: 
    print(dic["d"])
except KeyError:
    print("KeyError occured! Key not found in the dictionary")

try:
    print("Sup" + 9)
except TypeError:
    print("TypeError occured! Unsupported operand types.")

# Task 3 
try:
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))
    val = n1 / n2

except ValueError:
    print("Must enter an number")

except ZeroDivisionError:
    print("Cannot divide by 0")

else:
    print(f"The result is {val}")

finally:
    print("This block always executes")