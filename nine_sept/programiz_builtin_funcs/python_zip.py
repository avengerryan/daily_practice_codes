
# Python zip() : returns an iterator of tuples
# the zip() function takes iterables (can be zero or more), aggregates them in a
# tuple, and return it.


# zip(*iterables)


"""

# e.g. 1: Python Zip()

number_list = [1, 2, 3]
str_list = ['one', 'two', 'three']

# no iterables are passed
result = zip()

# print(result)

# converting iterator to list
result_list = list(result)
print(result_list)


# two iterables are passed
result = zip(number_list, str_list)

# converting iterator to set
result_set = set(result)
print(result_set)

"""


"""

# e.g.2: different no. of iterable elements

numbersList = [1, 2, 3]
str_list = ['one', 'two']
numbers_tuple = ('ONE', 'TWO', 'THREE', 'FOUR')

# Notice, the size of numbersList and numbers_tuple is different
result = zip(numbersList, numbers_tuple)

# converting to set
result_set = set(result)
print(result_set)

result = zip(numbersList, str_list, numbers_tuple)

# converting to set
result_set = set(result)
print(result_set)

"""





# zip(*zippedList) : the * operator can be used in conjunction with zip() to unzip
# the list

# e.g. 3: unzipping the value using zip()

coordinate = ['x', 'y', 'z']
value = [3, 4, 5]

result = zip(coordinate, value)
result_list = list(result)
print(result_list)


c, v = zip(*result_list)
print('c =', c)
print('v =', v)




























































