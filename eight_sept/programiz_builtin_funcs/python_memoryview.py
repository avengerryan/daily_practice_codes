
# python memoryview() : returns memory view of an argument
# The memoryview() function returns a memory view object of the given argument



"""

# example 1: how memoryview() works in python

# random bytearray
random_byte_array = bytearray('ABC', 'utf-8')

mv = memoryview(random_byte_array)

# access memory view's zeroth index
print(mv[0])

# create byte form memory view
print(bytes(mv[0:2]))

# create list from memory view
print(list(mv[0:3]))

"""





# Example 2: modify internal data using memory view

# random bytearray
random_byte_array = bytearray('ABC', 'utf-8')
print('Before updation:', random_byte_array)

mv = memoryview(random_byte_array)

# update 1st index of mv to z
mv[1] = 90
print('After updation:', random_byte_array)































