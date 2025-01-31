### File 5: Functions and Modules


# Inbuilt functions
# int()
# float()
# str()
# print()...



# Functions
# Definition: Functions are reusable blocks of code that perform tasks.
def printName(name='Boss'):
    print('Hello ' + name)

printName('Saif')
printName()

# Modules
# Definition: Modules are external files that contain Python code.
from math import sqrt, pow, factorial, pi, sin, cos, tan, log, log10, log2, e
import math
print(dir(math))
print(sqrt(16))
print(pow(2, 3))
print(factorial(5))
print(pi)
print(sin(90))