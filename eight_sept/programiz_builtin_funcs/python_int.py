
# Python int(): returns integer from a number or string

# the int() method returns an integer object from any number or string

"""

# example 1: how int() works in Python

# integer
print("int(123) is:", int(123))

# float
print("int(123.23) is:", int(123.23))

# string
print("int('123') is:",int('123'))


"""


"""
# example 2: how int() works for decimal, octal and hexadecimal

# binary 0b or 0B
print("For 1010, int is:", int('1010', 2))

# octal 0o or oo
print("For 12, int is:", int('12', 8))
print("For 0o12, int is:", int('0o12', 8))

# hexadecimal
print("For A, int is:", int('A', 16))
print("For oxA, int is:", int('0xA', 16))

"""




# example 3: int() for custom objects

class Person:
    age = 23

    def __index__(self):
        return self.age

    def __int__(self):
        return self.age

person = Person()
print('int(person) is:', int(person))




















