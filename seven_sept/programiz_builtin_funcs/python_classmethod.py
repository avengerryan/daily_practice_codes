
# python classmethod():
# the classmethod() method returns a class method for the given function


# Syntax: classmethod(function)

# NOTE: classmethod() is considered un-Pythonic so in newer python versions,
# you can use the @classmethod decorator for classmethod definition


# syntax: @classmethod
#         def func)cls, args...)


# classmethod() method takes a single parameter i.e. function, that needs to be converted into a class method

# a classmethod is a method that is bound to a class rather than its object.


# Class.classmethod()
# or
# Class().classmethod()


# Create class method using classmethod()


class Person:
    age = 25

    def printAge(cls):
        print('the age is:', cls.age)

# create printAge class method
Person.printAge = classmethod(Person.printAge)

Person.printAge()

































