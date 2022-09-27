## Exercise 35 - Working with math

# Write a program that takes two numbers (x and y) from the user and calculates
# new values with the help of the math functions on the previous slides
# (exp, log, log2, log10, pow, sqrt, cos, sin, tan, acos, asin, atan)
# Print out the results
# Combine all results in a list and create either a Scatter or a Line plot with them (optional)
import math
import matplotlib.pyplot as plt

def Math_Ops(x,y):
    result = list()
    value = math.exp(x)
    result.append(value)
    print(f"e to the power of {x} is {math.exp(x)}")

    value = math.exp(y)
    result.append(value)
    print(f"e to the power of {y} is {math.exp(y)}")

    value = math.log(x)
    result.append(value)
    print(f"log of {x} is {math.log(x)}")

    value = math.log(y)
    result.append(value)
    print(f"log of {y} is {math.log(y,x)}")

    value = math.cos(x)
    result.append(value)
    print(f"The cosine of {x} is {math.cos(x)}")

    value = math.cos(y)
    result.append(value)
    print(f"The cosine of {y} is {math.cos(y)}")

    value = math.sin(x)
    result.append(value)
    print(f"The sinus of {x} is {math.sin(x)}")

    value = math.sin(y)
    result.append(value)
    print(f"The sinus of {y} is {math.sin(y)}")

    value = math.tan(x)
    result.append(value)
    print(f"The tangens of {x} is {math.tan(x)}")

    value = math.tan(y)
    result.append(value)
    print(f"The tangens of {y} is {math.tan(y)}")

    if x > 0:
        value = math.pow(x,y)
        result.append(value)
        print(f"{x} to the power of {y} is {math.pow(x,y)}")

        value = math.log2(x)
        result.append(value)
        print(f"log of {x} to the base of 2 is {math.log2(x)}")

        value = math.log10(x)
        result.append(value)
        print(f"log of {x} to the base of 10 is {math.log10(x)}")

    if y > 0:
        value = math.pow(y,x)
        result.append(value)
        print(f"{y} to the power of {x} is {math.pow(y,x)}")

        value = math.log2(y)
        result.append(value)
        print(f"log of {y} to the base of 2 is {math.log2(y)}")

        value = math.log10(y)
        result.append(value)
        print(f"log of {y} to the base of 10 is {math.log10(y)}")

    if x >= 0:
        value = math.sqrt(x)
        result.append(value)
        print(f"The square root of {x} is {math.sqrt(x)}")
        
    if y >= 0:
        value = math.sqrt(y)
        result.append(value)
        print(f"The square root of {y} is {math.sqrt(y)}")

    if x > -1 and x < 1:
        value = math.acos(x)
        result.append(value)
        print(f"The acosine of {x} is {math.acos(x)}")

        value = math.asin(x)
        result.append(value)
        print(f"The asinus of {x} is {math.asin(x)}")

    if y > -1 and y < 1:
        value = math.acos(y)
        result.append(value)
        print(f"The acosine of {y} is {math.acos(y)}")

        value = math.asin(y)
        result.append(value)
        print(f"The asinus of {y} is {math.asin(y)}")

    if x != 0:
        value = math.atan(x)
        result.append(value)
        print(f"The atangens of {x} is {math.atan(x)}")

    if y != 0:
        value = math.atan(y)
        result.append(value)
        print(f"The atangens of {y} is {math.atan(y)}")
    return result


x = int(input("X: "))
y = int(input("Y: "))
result = Math_Ops(x,y)

plt.scatter(result, range(len(result)))
plt.show()

## Exercise 36 - Working with constants

# Write a second program that takes again two numbers from the user and calculates
# new values with the help of the same functions as in exercise 35
# This time the input variables have to multiplied by one of three shown constants (Pi, Euler number or Tau)
# Let the user choose which constant should be used
# Print out the results
# Combine all results in a list and create either a Scatter or a Line plot with them (optional)

user_input = input("\nNow choose a constant by which your values both should be multiplied.\nPi, Euler or Tau:")
invalid_input = True

while invalid_input == True:
    if user_input == "Pi":
        x *= math.pi
        y *= math.pi
        invalid_input = False
    elif user_input == "Euler":
        x *= math.e
        y *= math.e
        invalid_input = False
    elif user_input == "Tau":
        x *= math.tau
        y *= math.tau
        invalid_input = False
    else:
        print("Invalid Input")

print(f"Your new values are {x} and {y}")

result = Math_Ops(x,y)

plt.scatter(result, range(len(result)))
plt.show()
