

# Python id() : returns identity(unique integer) of an object
# id() function returns the identity of the object.
# this is an integer that is unique for the given object and remains constant during its lifetime


"""
# example 1: How id() works

class Foo:
    b = 5

dummyFoo = Foo()
print('id of dummyFoo =', id(dummyFoo))


"""



# Examples:

print('id of 5 =', id(5))

a = 5
print('id of a =', id(a))

b = a
print('id of b =', id(b))

c = 5.0
print('id of c =', id(c))

















