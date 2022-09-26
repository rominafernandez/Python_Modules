## Exercise 35 - Working with math

# Write a program that takes two numbers (x and y) from the user and calculates
# new values with the help of the math functions on the previous slides
# (exp, log, log2, log10, pow, sqrt, cos, sin, tan, acos, asin, atan)
# Print out the results
# Combine all results in a list and create either a Scatter or a Line plot with them (optional)
import math

x = int(input("X: "))
y = int(input("Y: "))

if x > 1 and y > 1:
    print(f"e to the power of {x} is {math.exp(x)}")
    print(f"e to the power of {y} is {math.exp(y)}")
    print(f"{x} to the power of {y} is {math.pow(x,y)}")
    print(f"{y} to the power of {x} is {math.pow(y,x)}")

    print(f"log of {x} to the base of {y} is {math.log(x,y)}")
    print(f"log of {y} to the base of {x} is {math.log(y,x)}")
    print(f"log of {x} to the base of 2 is {math.log2(x)}")
    print(f"log of {y} to the base of 2 is {math.log2(y)}")
    print(f"log of {x} to the base of 10 is {math.log2(x)}")
    print(f"log of {y} to the base of 10 is {math.log2(y)}")

    print(f"The square root of {x} is {math.sqrt(x)}")
    print(f"The square root of {y} is {math.sqrt(y)}")

    print(f"The cosine of {x} is {math.cos(x)}")
    print(f"The cosine of {y} is {math.cos(y)}")
    print(f"The sinus of {x} is {math.sin(x)}")
    print(f"The sinus of {y} is {math.sin(y)}")
    print(f"The tangens of {x} is {math.tan(x)}")
    print(f"The tangens of {y} is {math.tan(y)}")

if x <= 1:
    print(f"The acosine of {x} is {math.acos(x)}")
    print(f"The asinus of {x} is {math.asin(x)}")
    print(f"The atangens of {x} is {math.atan(x)}")

if y <= 1:
    print(f"The acosine of {y} is {math.acos(y)}")
    print(f"The asinus of {y} is {math.asin(y)}")
    print(f"The atangens of {y} is {math.atan(y)}")

## Exercise 36 - Working with constants

# Write a second program that takes again two numbers from the user and calculates
# new values with the help of the same functions as in exercise 35
#This time the input variables have to multiplied by one of three shown constants (Pi, Euler number or Tau)
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

if x > 1 and y > 1:
    print(f"e to the power of {x} is {math.exp(x)}")
    print(f"e to the power of {y} is {math.exp(y)}")
    print(f"{x} to the power of {y} is {math.pow(x,y)}")
    print(f"{y} to the power of {x} is {math.pow(y,x)}")

    print(f"log of {x} to the base of {y} is {math.log(x,y)}")
    print(f"log of {y} to the base of {x} is {math.log(y,x)}")
    print(f"log of {x} to the base of 2 is {math.log2(x)}")
    print(f"log of {y} to the base of 2 is {math.log2(y)}")
    print(f"log of {x} to the base of 10 is {math.log2(x)}")
    print(f"log of {y} to the base of 10 is {math.log2(y)}")

    print(f"The square root of {x} is {math.sqrt(x)}")
    print(f"The square root of {y} is {math.sqrt(y)}")

    print(f"The cosine of {x} is {math.cos(x)}")
    print(f"The cosine of {y} is {math.cos(y)}")
    print(f"The sinus of {x} is {math.sin(x)}")
    print(f"The sinus of {y} is {math.sin(y)}")
    print(f"The tangens of {x} is {math.tan(x)}")
    print(f"The tangens of {y} is {math.tan(y)}")

if x <= 1:
    print(f"The acosine of {x} is {math.acos(x)}")
    print(f"The asinus of {x} is {math.asin(x)}")
    print(f"The atangens of {x} is {math.atan(x)}")

if y <= 1:
    print(f"The acosine of {y} is {math.acos(y)}")
    print(f"The asinus of {y} is {math.asin(y)}")
    print(f"The atangens of {y} is {math.atan(y)}")
