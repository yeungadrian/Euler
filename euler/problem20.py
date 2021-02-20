'''
Find the sum of the digits in the number 100!
'''

import numpy as np

def calculate_sum_digits_factorial(x):
    factorial = np.math.factorial(x)
    result = sum(map(int, str(factorial)))

    return result

print(calculate_sum_digits_factorial(100))
