#Lattice paths

''' For an nxn grid, you will need to move n times right and n times down to move from top left to bottom right
and so 2n moves
If there was any order of the moves then it would be 2n!


'''

import math

def latticepaths(n):
    n_factorial = math.factorial(n)
    return math.factorial(2 * n) / (n_factorial * n_factorial)

print(latticepaths(20))