
# python repr() : returns a printable representation of the object.
# the repr() function returns a printable representation of the given object

# repr(obj)


"""

# e.g. 1: how repr() works in python

var = 'foo'

print(var)
print(repr(var))

# by eval() we will get the original object
print(eval(repr(var)))

"""



# e,g 2: implement __repr__() for custom objects.

class Person:
    name = 'Adam'

    def __repr__(self):
        return repr('Hello ' + self.name)


print(repr(Person()))



















