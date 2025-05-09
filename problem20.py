"""
Find the sum of the digits of 100!
"""

import math


print(sum([int(x) for x in str(math.factorial(100))]))
