# Erick Sun
# Project 1: Eligible Elector

# Asking user for age
age = int(input("How old are you? "))

# Verify valid age
if age < 0:
    print("That's not a valid age!")  

# If age is > or = to 18, print statement 1
elif age >= 18:
    print("Congratulations!You are eligible to vote. Go make a difference!")

# Else (meaning they are less than 18) print statement 2
else:
    print(f"Oops! You're not eligible yet. But hey, only {18 - age} more year(s) to go!")