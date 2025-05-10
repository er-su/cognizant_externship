# Erick Sun

# Task 1 - Variables
name = "Spaghetti"
age = 1000
height = 6.0

print(f"Hey there, my name is {name}! I'm {age} years old and {height} feet tall.")

# Task 2- Operators: Playing with Numbers
num1 = 1e13
num2 = 1e2

# Adding together the two values
num_sum = num1 + num2
# Subtracting the two values
num_dif = num1 - num2
# Multiplying the two values
num_prod = num1 * num2
# Dividing the two values
num_quot = num1 / num2

print(f"The sum of {num1} and {num2} is {num_sum}")
print(f"The difference of {num1} and {num2} is {num_dif}")
print(f"The product of {num1} and {num2} is {num_prod}")
print(f"The quotient of {num1} and {num2} is {num_quot}")

# Task 3 - Conditional Statements
guess = float(input("Give me a number: "))

if guess == 0.0:
    print("Zero it is. A perfect balance!")
elif guess > 0.0:
    print("This number is positive. Awesome!")
else:
    print("This number is negative. Better luck next time!")