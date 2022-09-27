## Exercise 39 - Pandas DataFrames

# Write a program that creates a DataFrame consisting of at least 4 rows and 6 columns
# It should contain random numbers generated via NumPy
# Create 6 new DataFrames by sorting the original DataFrame alongside the columns (df.sort_values())
# Let the program print a description of the original DataFrame
# What do these numbers mean?
# Create a Scatter-Plot for each column

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame(np.random.randn(4,6),index = [1,2,3,4], columns = ["A", "B", "C", "D", "E", "F"])
print(df)
print(f"\nSorted by A: \n{df.sort_values(by='A')}")
print(f"\nSorted by B: \n{df.sort_values(by='B')}")
print(f"\nSorted by C: \n{df.sort_values(by='C')}")
print(f"\nSorted by D: \n{df.sort_values(by='D')}")
print(f"\nSorted by E: \n{df.sort_values(by='E')}")
print(f"\nSorted by F: \n{df.sort_values(by='F')}")

print(df.describe())

# Scatter Plots
for i in df.columns:
    plt.scatter(df[i],range(4))
    plt.show()

## Exercise 73 - Pandas and Files

# Use your DataFrame from Exercise 39 and save it to a csv- file and an Excel-file
# Try to read these files with the help of pandas afterwards

df.to_csv("Example_DF.csv", sep=";")
df.to_excel("Example_DF.xlsx")
df2 = pd.read_csv("Example_DF.csv", sep=";", index_col=0)
df3 = pd.read_excel("Example_DF.xlsx", index_col=0)
print(df2)
print(df3)
