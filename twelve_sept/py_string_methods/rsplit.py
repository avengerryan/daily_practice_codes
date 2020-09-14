
# python string rsplit() : splits string from right
# the rsplit() method splits string from the right at the specified and returns
# a list of strings

# str.rsplit([separator [, maxsplit]])








"""

# e.g. 1: how rsplit() works in Python

text = "Love thy neighbor"

# split at space
print(text.rsplit())

grocery = 'Milk, Chicken, Bread'

# splits at ','
print(grocery.rsplit(', '))

# splitting at ':'
print(grocery.rsplit(':'))

"""









# e.g.2: how split() works when maxsplit is specified

grocery = "Milk, Chicken, Bread, Butter"

# maxsplit: 2
print(grocery.rsplit(', ', 2))

# maxsplit: 1
print(grocery.rsplit(', ', 1))

# maxsplit: 5
print(grocery.rsplit(', ', 5))

# maxsplit: 0
print(grocery.rsplit(', ', 0))










































































