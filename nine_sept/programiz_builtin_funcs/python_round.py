
# python round() : rounds a no. to specified decimals.
# the round() function returns a floating point no. rounded to the specified no.
# of decimals


"""

# e.g. 1: how round() works in python

# for integers
print(round(10))

# for floating point
print(round(10.7))

# even choice
print(round(5.5))

"""


"""

# e.g. 2: round a no. to the given no. of decimal places

print(round(2.665, 2))
print(round(2.675, 2))

"""


# For precision: use a module named as decimal

from decimal import Decimal

# normal float
num = 2.675
print(round(num, 2))

# using decimal.Decimal (passed float as string for precision)
num = Decimal('2.675')
print(round(num, 2))




