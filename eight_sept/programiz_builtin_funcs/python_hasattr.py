
# Python hasattr() : returns whether object has named attribute

# example: how hasattr() works in Python


class Person:
    age = 23
    name = 'Adam'

person = Person()

print('Person has age?:', hasattr(person, 'age'))
print('Person has salary?:', hasattr(person, 'salary'))