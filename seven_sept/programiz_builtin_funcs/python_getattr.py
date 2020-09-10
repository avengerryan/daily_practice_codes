
# python getattr()
# returns value of named attribute of an object

# the getattr() method returns the value of the named attribute of an object.
# If not found, it returns the default value provided to the function.

# how getattr() works in Python

"""
class Person:
    age = 23
    name = "Adam"

person = Person()
print('the age is: ', getattr(person, 'age'))
print('the age is:', person.age)

"""


# example 2: getattr() when named attribute is not found

class Person:
    age = 23
    name = 'Adam'

person = Person()

# when default value is provided
print('the sex is: ', getattr(person, 'sex', 'Male'))


# when no default value is provided
print('the sex is: ', getattr(person, 'sex'))

























