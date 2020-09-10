
# Python dictionary get(): returns value of the key
# the get() method returns the value for the specified key
# if key is in dictionary.



"""

# e.g. 1: how get() works for dictionaries

person = {'name': 'Phill', 'age': 22}

print('Name: ', person.get('name'))
print('Age: ', person.get('age'))


# value is not provided
print('Salary: ', person.get('salary'))

# value is provided
print('Salary: ', person.get('salary', 0.0))

"""




# Python get() method vs dict[key] to access elements

person = {}

# using get() results in None
print('Salary: ', person.get('salary'))

# using [] results in keyError
print(person['salary'])










