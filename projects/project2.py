# Erick Sun
# Project 2: Number Guessing Game

import random
number_to_guess = random.randint(1, 100)
num_guesses = 0
while(True):
    guess = int(input("Guess an integer from 1-100: "))

    if guess < number_to_guess:
        print("Too low! Try again.")
        num_guesses += 1
        
    elif guess > number_to_guess:
        print("Too high! Try again.")
        num_guesses += 1

    else:
        print(f"Congratulations! You guessed it in {num_guesses} attempts!")
        break
