# Write a program to demonstrate different import mechanisms in Python

# 1. Import the entire module
import math
print("Square root:", math.sqrt(25))

# 2. Import a specific function
from math import factorial
print("Factorial:", factorial(5))

# 3. Import with an alias
import math as m
print("Power:", m.pow(2, 3))

# 4. Import multiple functions
from math import ceil, floor
print("Ceiling:", ceil(4.2))
print("Floor:", floor(4.8))

# 5. Import all names from a module
from math import *
print("Absolute value:", fabs(-10))
