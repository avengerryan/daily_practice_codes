
# Python vars() : returns the __dict__ attribute.
# the vars() function returns the __dict__ attribute of the given object.


# vars(object)

# e.g.: working of python vars()

class Foo:
    def __init__(self, a=5, b=10):
        self.a = a
        self.b = b

object = Foo()
print(vars(object))

































