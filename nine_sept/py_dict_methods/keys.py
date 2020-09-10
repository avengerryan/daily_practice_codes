
# Python dictionary keys() : returns view object of all keys
# the keys() method returns a view object that displays a list of all the keys
# in the dictionary.


"""

# e.g. 1: How keys() works

person = {'name': 'Phill', 'age': 22, 'salary': 3500.0}
print(person.keys())

empty_dict = {}
print(empty_dict.keys())

"""





# e.g. 2: How keys() works when dictionary is updated

person = {'name': 'Phill', 'age': 22}

print('before dictionary is updated')
keys = person.keys()
print(keys)

# adding an element to the dictionary
person.update({'salary': 3500.0})
print('\nAfter dictionary is updated')
print(keys)






