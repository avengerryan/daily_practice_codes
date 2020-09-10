







# Python format()
# returns formatted representation of a value


"""
# Number formatting with format()

# d, f and b are type

# integer
print(format(123, 'd'))

# float arguments
print(format(123.4567898, 'f'))

# binary format
print(format(12, 'b'))

"""


'''
# example: number formatting with fill, align, sign, width, precision and type

# integer
print(format(1234, "*>+7,d"))

# float number
print(format(123.4567, "^-09.3f"))

'''



# Example: using format() by overriding __format__()


# custom __format__() method

class Person:
    def __format__(self, format):
        if (format == 'age'):
            return '23'

print(format(Person(), 'age'))












