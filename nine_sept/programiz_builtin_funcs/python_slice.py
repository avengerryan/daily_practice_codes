
# Python slice() : returns a slice object.
# the slice() function returns a slice object that can use used to slice strings,
# lists, tuple etc

# slice(start, stop, step)


"""

# e.g. 1: create a slice object for slicing

# contains indices (0, 1, 2)

result = slice(3)
print(result)

# contains indices (1, 3)
result2 = slice(1, 5, 2)
print(slice(1, 5, 2))

"""



"""

# e.g. 2: get substring using slice object

# program to get substring from the given string

py_string = 'Python'

slice_object = slice(3)
print(py_string[slice_object])

# stop = 3
# contains 0, 1 and 2 indices
slice_object = slice(1, 6, 2)
print(py_string[slice_object])

"""


"""

# e.g. 3: Get substring using negative index

py_string = 'Python'

slice_object = slice(-1, -4, -1)

print(py_string[slice_object])

"""



"""

# e.g. 4: get sublist and sub tuple

py_list = ['p', 'y', 't', 'o', 'n']
py_tuple = ('p', 'y', 't', 'h', 'o', 'n')

# contains indices 1 and 3
slice_object = slice(3)
print(py_list[slice_object])

# contains indices 1 and 3
slice_object = slice(1, 5, 2)
print(py_tuple[slice_object])

"""

"""

# e.g. 5: get sublist and subtuple using negatice index

py_list = ['p', 'y', 't', 'h', 'o', 'n']
py_tuple = ('p', 'y', 't', 'h', 'o', 'n')

# contains indices -1, -2 and -3
slice_object = slice(-1, -4, -1)
print(py_list[slice_object])

# contains indices -1 and -3
slice_object = slice(-1, -5, -2)
print(py_tuple[slice_object])

"""


# e.g. 6: using indexing syntax for slicing

# obj[start:stop:step}

py_string = 'Python'

# contains indices 0, 1, and 2
print(py_string[0:3])

# contains indices 1 and 3
print(py_string[1:5:2])






































