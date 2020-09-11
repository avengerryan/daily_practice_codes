
# Python dictionary setdefault() : Inserts key with a value if key is not present.

# the setdefault() method returns the value of a key (if the key is in dictionary)
# If not, it inserts key with a value to the dictionary.

# dict.setdefault(key[, default_value])



"""

# e.g. 1: how setdefault() works when key is in the dictionary

person = {'name': 'Phill', 'age': 22}

age = person.setdefault('age')
print('person =', person)
print('Age =', age)

"""





# e.g. 2: how setdefault() works when key is not in the dictionary

person = {'name': 'Phill'}

# key is not in the dictionary
salary = person.setdefault('salary')
print('person =', person)
print('salary = ', salary)

# key is not in the dictionary
# default_value is provided
age = person.setdefault('age', 22)
print('person = ', person)
print('age = ', age)













