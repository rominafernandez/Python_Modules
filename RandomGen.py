## Exerise 37 - Random generator

# Write a program that generates several random numbers
# Let the user input the ranges for three random integers
# Let the user choose how many random floats between 0 and 1 should be created
# Let the user put in at least two mu and two sigma to create normal distribution values
# What happens if you switch these two values?
# Last but not least put all generated values in a list, print the list, shuffle the list and print it again
# Create Bar-Plots for this list (before and after the shuffle)
import matplotlib.pyplot as plt
import random
result = list()

# Three random int with user input ranges
print("Specify three ranges by which a random number should be generated.")

for i in range(3):
    user_input = input(f"Range {i+1}: ").split("-")
    rand_int = random.randint(int(user_input[0]), int(user_input[1]))
    result.append(rand_int)


# number of random floats
user_input = int(input("How many random floats between 0 and 1 should be generated? \n"))

for i in range(user_input):
    rand_float= random.random()
    result.append(rand_float)


# Gaussian distribution
print("Specify two mu (mean) and sigma (standard deviation) pairs to create normal distribution values. Separate them by space.")

for i in range(2):
    user_input = input(f"mu sigma pair {i+1}: ").split()
    rand_int = random.gauss(int(user_input[0]), int(user_input[1]))
    rand_int_switch = random.gauss(int(user_input[1]), int(user_input[0]))
    result.append(rand_int)
    result.append(rand_int_switch)
    print(f"The normal distribution with mu = {user_input[0]} and sigma = {user_input[1]} is {rand_int}")
    print(f"If you switch the mu and sigma value you get {rand_int_switch}")

# Result list + shuffle and Bar-Plots 
print(f"\nHere is a list of all the generated values: \n{result}")
plt.bar(list(range(len(result))),result)
plt.show()

random.shuffle(result)
print(f"After shuffling it looks like this: \n{result}")
plt.bar(list(range(len(result))),result)
plt.show()
