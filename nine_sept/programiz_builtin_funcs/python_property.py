
# Python property() : returns the property attribute

# property(fget=None, fset=None, fdel=None, doc=None)




"""

# eg 1:

class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        print('Getting name')
        return self._name

    def set_name(self, value):
        print('Setting name to ' + value)
        self._name = value

    def del_name(self):
        print('Deleting name')
        del self._name

    # set property to use get_name, set_name
    # and del_name methods

    name = property(get_name, set_name, del_name, 'Name property')

p = Person('Adam')
print(p.name)
p.name = 'John'
print(p.name)
del p.name
# print(p.name)

"""



# eg 2: Using @property decorator

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        print('Getting name')
        return self._name

    @name.setter
    def name(self, value):
        print('Setting name to ' + value)
        self._name = value

    @name.deleter
    def name(self):
        print('Deleting name')
        del self._name

p = Person('Adam')
print('The name is:', p.name)
p.name = 'John'
del p.name






