
# Python dictionary fromkeys() : creates dictionary from given sequence.
# the fromkeys() method creates a new dictionary from the given sequence of
# elements with a value provided by the user.


# dictionary.fromkeys(sequence[, value])


"""

# e.g.1: Create a dictionary from a sequence of keys

# vowels keys
keys = {'a', 'e', 'i', 'o', 'u'}

vowels = dict.fromkeys(keys)
print(vowels)

"""


"""

# e.g. 2: create a dictionary from a sequence of keys with value

# vowels keys
keys = {'a', 'e', 'i', 'o', 'u'}
value = 'vowel'

vowels = dict.fromkeys(keys, value)
print(vowels)

"""




"""

# e.g. 3: create a dictionary from mutable object list

# vowel keys
keys = {'a', 'e', 'i', 'o', 'u'}
value = [1]


vowels = dict.fromkeys(keys, value)
print(vowels)

# updating the value
value.append(2)
print(vowels)

"""





# Dictionary comprehension:

# vowels keys
keys = {'a', 'e', 'i', 'o', 'u'}
value = [1]

vowels = { key : list(value) for key in keys }
# you can also use { key : value[:] for key in keys }
print(vowels)


# updating the value
value.append(2)
print(vowels)






































