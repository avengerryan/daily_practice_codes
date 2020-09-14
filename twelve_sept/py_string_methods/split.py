
# python string split() : splits string from left
# the split() method breaks up a string at the specified separator and returns a
# list of strings

# str.split([separator [, maxsplit]])






"""

# e.g.1: how split() works in python

text = "Love thy neighbor"

# splits at space
print(text.split())

grocery = "Milk, Chicken, Bread"

# splits at ','
print(grocery.split(', '))

# splitting at ':'
print(grocery.split(': '))

"""








# e.g.2: How split() works when maxsplit is specified

grocery = "Milk, Chicken, Bread, Butter"

# maxsplit: 2
print(grocery.split(', ', 2))

# maxsplit: 1
print(grocery.split(', ', 1))

# maxsplit: 5
print(grocery.split(', ', 5))

# maxsplit: 0
print(grocery.split(', ', 0))



















































































































































