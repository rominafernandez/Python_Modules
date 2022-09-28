## Group Exercise 07 - DataFrames and Plots

# Create an empty DataFrame
# At least 10 columns and 25 rows
# User specifies correct number of rows and columns
# Fill each column either with:
# A random numpy array
# Or by hand from user inputs (nested while loops)
# Calculate sums, minimum and maximum values for each column
# Plot each column as scatter plot, each row as line plot and
# sums, minimum and maximum values as bar plots
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a DataFrame with user_input
user_dimensions = input("Type in the dimensions of your DataFrame.\nRows Columns: ").split()
user_input = input("Do you want your DataFrame to be filled with random numbers (rand) or fill them yourself (man)? \n")

if user_input == "rand":
    user_range = input("Type in a range for your random numbers. \nX Y: ").split()
    user_deci = input("Do you want integers (int) or floating point numbers (float)? \n")
    if user_deci == "int":
        user_df = pd.DataFrame(np.random.randint(float(user_range[0]), float(user_range[1]), size = (int(user_dimensions[0]), int(user_dimensions[1]))))
    if user_deci == "float":
        user_df = pd.DataFrame(np.random.uniform(float(user_range[0]), float(user_range[1]), size = (int(user_dimensions[0]), int(user_dimensions[1]))))

if user_input == "man":
    user_df = pd.DataFrame(index = range(int(user_dimensions[0])), columns = range(int(user_dimensions[1])))
    for i in range(int(user_dimensions[0])):
        user_input = input(f"Type in your {user_dimensions[1]} values for your {i+1}. row. \n").split()
        user_df.iloc[i][:] = user_input

print(f"\nHere is your DataFrame: \n{user_df}")


# Calculate and Plot sum, min and max of every column and plot
for i in range(len(user_df.columns)):
    sum_df = user_df.iloc[:][i].sum()
    min_df = user_df.iloc[:][i].describe()["min"]
    max_df = user_df.iloc[:][i].describe()["max"]

    x = ["Sum", "Min", "Max"]
    y = [sum_df, min_df, max_df]

    plt.figure(figsize=[4, 4])
    plt.bar(x,y)
    plt.title(f"Column {i}", fontsize=25)
    plt.tight_layout()
    plt.show()
    plt.close()

# Plotting columns as scatter-plot
for i in range(len(user_df.columns)):
    x = range(int(user_df.iloc[:][i].describe()["count"]))
    y = user_df.iloc[:][i]

    plt.figure(figsize=[4, 4])
    plt.scatter(x,y)
    plt.title(f"Column {i}", fontsize=25)
    plt.tight_layout()
    plt.show()
    plt.close()

# Plotting rows as line-plot
for i in range(len(user_df)):

    plt.figure(figsize=[4, 4])
    plt.plot(user_df.iloc[i][:])
    plt.title(f"Row {i}", fontsize=25)
    plt.tight_layout()
    plt.show()
    plt.close()
