
# Python type() : returns the type of the object
# the type() function either returns the type of the object or returns a new type
# object based on the arguments passed.



# the type function has 2 different forms:

# type(object)
# type(name, bases, dict)



"""

# e.g.1: get type of an object

numbers_list = [1, 2]
print(type(numbers_list))

numbers_dict = {1: 'one', 2: 'two'}
print(type(numbers_dict))

class Foo:
    a = 0

foo = Foo()
print(type(foo))

"""





# e.g. 2: create a type object

o1 = type('X', (object,), dict(a='Foo', b=12))

print(type(o1))
print(vars(o1))
    
class test:
    a = 'Foo'
    b = 12

o2 = type('Y', (test,), dict(a='Foo', b=12))
print(type(o2))
print(vars(o2))









































