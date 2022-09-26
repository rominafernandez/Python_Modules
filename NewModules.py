## Exercise 33 - New modules

# Write a program that asks the user to guess a specific number
# Generate a random number between 0 and 99, search the library to find a module and a function for this task
# Generate a while loop that asks for a guess as long as the user didn’t guess right
# Print out hints if the user is lower or higher than the random number
# Count the number of guesses the user needed and print them out after the user guessed correctly

import random

rand_int = random.randint(0,100)

user_input = int()
counter = 0
print("Guess what number is on my mind!")

while user_input != rand_int:
    user_input = int(input("Your guess: "))
    counter += 1
    if user_input < rand_int:
        print("Your guess was too low, try again.")
    elif user_input > rand_int:
        print("Your guess was too high, try again.")
    else:
        print(f"Correct! You got it in {counter} tries.")
