
# python set copy() : returns shallow copy of a set
# the copy() method returns a shallow copy of the set



"""

# using = operator

numbers = {1, 2, 3, 4}
new_numbers = numbers

print(new_numbers)

"""



"""

# NOTE:

numbers = {1, 2, 3, 4}
new_numbers = numbers

new_numbers.add(5)

print('numbers: ', numbers)
print('new_numbers: ', new_numbers)

"""






# e.g.1: how the copy() method works for sets

numbers = {1, 2, 3, 4}
new_numbers = numbers.copy()

new_numbers.add(5)

print('numbers: ', numbers)
print('new_numbers: ', new_numbers)


































