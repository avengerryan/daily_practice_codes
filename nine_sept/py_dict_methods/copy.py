
# python dictionary copy(): returns shallow copy of a dictionary
# they copy() method returns a shallow copy of the dictionary

# dict.copy()

"""

# e.g.1: how copy works for dictionaries

original = {1: 'one', 2: 'two'}
new = original.copy()

print('Original: ', original)
print(id(original))

print('New: ', new)
print(id(new))

"""


"""

# e.g. 2: using = operator to copy dictionaries

original = {1: 'one', 2: 'two'}
new = original

# removing all elements from the list
new.clear()

print('new: ', new)
print('Original: ', original)

# as we can see that, bcoz of using =, when we clear new dict,
# original dict is also cleared

"""



"""

# e.g.3: using copy() to copy dictionaries.

original = {1: 'one', 2: 'two'}
new = original.copy()

# removing all elements from the list
new.clear()

print('new: ', new)
print('original: ', original)

"""































