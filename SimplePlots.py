## Exercise 69 - Simple Plots

# Generate a Scatter, a Line and a Bar-Plot using Matplotlib
# Create also a Histogram
# You have at least 180 minutes (two lessons) to play around with this module to get accustomed to using it
# You have to install matplotlib beforehand in your terminal
# (pip install matplotlib)

import matplotlib.pyplot as plt

# Scatter Plot
x = [2,4,7,8,3,6,8,6,3,2,9,7]
y = [1,2,3,9,8,7,5,6,4,3,2,1]

plt.scatter(x, y)
plt.show()

# Line-Plot
points = [2,5,7,4,3,3,6,9,0,6,3]

plt.plot(points)
plt.show()

# Bar-Plot
x = ["A", "B", "C"]
y = [5,1,3]

plt.bar(x,y)
plt.show()

# Histogram
x = [1,6,1,3,4,4,5,6,6,6,1,4,3,5,8,5,6]

plt.hist(x)
plt.show()
