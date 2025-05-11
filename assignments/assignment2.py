# Erick Sun
# Explore Loops in Python

# Task 1 - Counting Down with Loops
countdown = int(input("Enter the starting number: "))
while(countdown > 0):
    print(countdown, end=" ")
    countdown -= 1

print("Blast off! 🚀")

# Task 2 - Multipllication Table with for Loops
mult = int(input("Enter a number: "))
for i in range(10):
    print(f"{mult} x {i + 1} = {(i + 1) * mult}")

# Task 3 - Find the Factorial
fact = int(input("Enter a number: "))
temp_fact = 1
for i in range (2, fact + 1):
    temp_fact *= i

print(f"The factorial of {fact} is {temp_fact}")