

# Python hash() : returns hash value of an object

# The hash() method returns the hash value of an object if it has one.

# hash values are just integers that are used to compare dictionary lookup quickly

# internally hash() method calls __hash__() method of an object which is set by default for any object.

"""
# How hash() works in python

# hash for integer unchanged
print('Hash for 181 is:', hash(181))

# hash for decimal
print('Hash for 181.23 is:', hash(181.23))

# hash for string
print('Hash for Python is:', hash('Python'))

"""

"""

# example 2: hash() for immutable tuple object

# hash() method works only for immutable objects as tuple

# tuple of vowels
vowels = ('a', 'e', 'i', 'o', 'u')

print('The hash is:', hash(vowels))

"""


# example 3: hash() for custom objects by overriding __hash__()

class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def __eq__(self, other):
        return self.age == other.age and self.name == other.name

    def __hash__(self):
        print('The hash is:')
        return hash((self.age, self.name))


person = Person(23, 'Adam')

print(hash(person))




















