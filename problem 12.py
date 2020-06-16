

from functools import reduce

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

triangle_number = 1
num_factors = len(factors(triangle_number))
x = 1
while (num_factors < 500):
    x = x + 1
    triangle_number = triangle_number + x
    num_factors = len(factors(triangle_number))

print(triangle_number)
