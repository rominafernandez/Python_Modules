## Exercise 38 - NumPy arrays

# Write a simple python program that generates the following arrays:
# An array consisting of 25 zeros
# An array consisting of 8 ones
# An array consisting of numbers from 0 to 24 in order
# An array consisting of 9 entries of your choice
# An two-dimensional array TD consisting of 6 rows of arrays with 5 entries each
# A transposed version of the two-dimensional array TD
# Write furthermore an algorithm to print out the sum, maximum value, minimum value and shape of all created arrays

## Exercise 80 - Mathematics with NumPy

# Use the arrays from Exercise 38 and run some mathematical functions like np.sin with them
import numpy as np

Ar1 = np.zeros(25)
Ar2 = np.ones(8)
Ar3 = np.arange(25)
Ar4 = np.array([5,2,8,7,5,3,4,12,13,14])
Ar5 = np.arange(30).reshape(6,5)
Ar6 = Ar5.transpose()

def Array_Calc(input_array):
    print(f"Input array: \n{input_array}")
    print(f"Sum: {input_array.sum()}")
    print(f"Max: {input_array.max()}")
    print(f"Min: {input_array.min()}")
    print(f"Shape: {input_array.shape}")
    print(f"Sinus: \n{np.sin(input_array)}")
    print(f"Cosinus: \n{np.cos(input_array)}")
    print(f"Tangens: \n{np.tan(input_array)}")
    print(f"Log10: \n{np.log10(input_array)}")
    print(f"Log2: \n{np.log2(input_array)}")
    print(f"Square root: \n{np.sqrt(input_array)}")
    print(f"Exponent: \n{np.exp(input_array)}")
    print(f"To the power of 2: \n{np.power(input_array, 2)}")
    print(f"Fourier Transformation: \n{np.fft.fft(input_array)}")
    print()

Array_Calc(Ar1)
Array_Calc(Ar2)
Array_Calc(Ar3)
Array_Calc(Ar4)
Array_Calc(Ar5)
Array_Calc(Ar6)
