
# python setattr() : Sets the value of an attribute of an object
# the setattr() function sets the value of the attribute of an object


# setattr(object, name, value)



"""

# e.g. 1: how setattr() works in python


class Person:
    name = 'Adam'

p = Person()
print('Before modification:', p.name)

# setting name to 'John'
setattr(p, 'name', 'John')

print('After modification:', p.name)

"""




# e.g. 2: when the attribute is not found in setattr()

class Person:
    name = 'Adam'

p = Person()

# setting attribute name to John
setattr(p, 'name', 'John')
print('Name is:', p.name)

# setting an attribute not present in Person
setattr(p, 'age', 23)
print('Age is:', p.age)

































