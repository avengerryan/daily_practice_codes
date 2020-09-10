
# Python max() : returns the largest item

# the python max() function returns the largest item in an iterable.
# python max() function can also be used to find the largest item between 2 or more parameters



"""
# example 1: get the largest item in a list

number = [3, 2, 8, 5, 10, 6]
largest_number = max(number)

print('the largest number is:', largest_number)

"""



"""

# example 2: the largest string in a list

languages = ['Python', 'C Programming', 'Java', 'JavaScript']
largest_string = max(languages)

print('the largest string is:', largest_string)

"""


"""

# example 3: max() in dictionaries

square = {2: 4, -3: 9, -1: 1, -2: 4}

# the largest key
key1 = max(square)
print('the largest key:', key1)

# the key whose value is the largest
key2 = max(square, key = lambda k: square[k])

print('the key with the largest value:', key2)

# getting the largest value
print('the largest value:', square[key2])

"""



# example 4: find the maximum among the given numbers

result = max(4, -5, 23, 5)
print('the maximum number is:', result)



















