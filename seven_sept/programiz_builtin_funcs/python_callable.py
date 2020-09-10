
# Python callable()
# checks if the object is callable


# the callable() method returns True if the object passed appears callable.
# if not, true it returns False


# syntax: callable(object)


x = 5
print(callable(x))

print(30*'=')

def testFunction():
    print("Test")

y = testFunction
print(callable(y))

# Here appears to be callable, but may not be callable.

print(30*'=')



# callable object

class Foo:
    def __call__(self):
        print('print something')

print(callable(Foo))


print(30*'=')


class Foo:
    def __call__(self):
        print('print something')

InstanceOfFoo = Foo()

# Prints 'Print Something'

InstanceOfFoo()
print(InstanceOfFoo)

raw = InstanceOfFoo()

print(raw)


print(30*'=')

# example:

# object appears to be callable but isn't callable.

class Foo:
    def printLine(self):
        print('Print Something')

print(callable(Foo))


print(30*'=')

class Foo:
    def printLine(self):
        print('Print Something')

print(callable(Foo))

InstanceOfFoo = Foo()

# Raises an Error
# 'Foo' object is not callable
InstanceOfFoo()

