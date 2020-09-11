
# python list index() : returns the index of the element in the list
# the index() method returns the index of the specified element in the list.

# list.index(element, start, end)



"""

# e.g.1: find the index of the element

# vowels list
vowels = ['a', 'e', 'i', 'o', 'u']

# index of 'e' in vowels
index = vowels.index('e')
print('The index of e: ', index)

# element 'i' is searched
# index of the first 'i' is returned
index = vowels.index('i')

print('The index of i: ', index)

"""



"""

# e.g.2: index of the element not present in the list

# vowels list
vowels = ['a', 'e', 'i', 'o', 'u']

# index of 'p' is vowels
index = vowels.index('p')
print('The index od p: ', index)

"""





# e.g. 3: working of index() with start and end parameters

# alphabets list
alphabets = ['a', 'e', 'i', 'o', 'g', 'l', 'i', 'u']


# index of 'i' in alphabets
index = alphabets.index('e')
print('The index of e: ', index)

# 'i' after the 4th index is searched
index = alphabets.index('i', 4)
print('The index of i: ', index)

# 'i' between 3rd and 5th index is searched
index = alphabets.index('i', 3, 5)
print('The index of i: ', index)



























