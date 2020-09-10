
# python oct(): returns ocatal representation of an integer
# the oct() function takes an integer number and returns its octal representation.


"""

# example 1: how oct() works in python

# decimal to octal
print('oct(10) is:', oct(10))

# binary to octal
print('oct(0b101) is:', oct(0b101))

# hexadecimal to octal
print('oct(0XA) is:', oct(0XA))

"""



# example 2: oct() for custom objects

class Person:
    age = 23

    def __index__(self):
        return self.age

    def __int__(self):
        return self.age

person = Person()
print('the oct is:', oct(person))


















