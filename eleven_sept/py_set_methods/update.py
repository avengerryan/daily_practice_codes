
# python set update() : add elements to the set
# the python set update() method updates the set, adding items from other iterables.


# A.update(iterable)





"""

# e.g.1: python set update()

A = {'a', 'b'}
B = {1, 2, 3}

result = A.update(B)

print('A =', A)
print('result =', result)

"""







# e.g.2: add elements of string and dictionary to set

string_alphabet = 'abc'
numbers_set = {1, 2}

# add elements of the string to the set
numbers_set.update(string_alphabet)

print('numbers_set =', numbers_set)

info_dictionary = {'key': 1, 'lock': 2}
numbers_set = {'a', 'b'}

# add keys of dictionary to the set
numbers_set.update(info_dictionary)
print('numbers_set', numbers_set)

























































