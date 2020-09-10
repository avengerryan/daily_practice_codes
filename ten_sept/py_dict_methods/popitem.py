
# Python dictionary popitem() : Returns and removes latest element from dictionary.
# the python popitem() method removes and returns the last element (key, value)
# pair inserted into the dictionary.


# dict.popitem()

# popitem() method removes and returns the pair from the dictionary
# in LIFO order.





"""

# e.g. 1: working of popitem() method

person = {'name': 'Phill', 'age': 22, 'salary': 3500.0}

result = person.popitem()

print('poped, Result value = ', result)
print('After popitem, person =', person)

print(30*'=')

# inserting a new element pair
person['profession'] = 'Plumber'

result = person.popitem()

print('Return value, after inserting = ', result)
print('person = ', person)

"""




# e.g. 2: if dictionary is empty

empt_dict = {}

result = empt_dict.popitem()

print(result)





































