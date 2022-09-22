"""
This was a very cool problem.  

"Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?"

Through research, found out that a nxn lattice from 1 corner to the opposite has (2n!)/((n!)(n!)) paths.  This is just a pythonic representation of that.
Also helped me practice building functions, which I have been putting off.
"""
import math               #Math module has that sweet factorial
def lattice(n):
    k = (math.factorial(2 * int(n))) / ((math.factorial(int(n))) * (math.factorial(int(n))))
    print("There are " + str(k) + " paths in this lattice.")
n = input("What is the value of n? ")
lattice(n)
