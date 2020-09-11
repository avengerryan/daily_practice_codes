
# python list pop() : removes element at the given index
# the pop() method removes the item at the given index from the list and returns
# the removed item.

# list.pop(index)



"""

# e.g. 1: pop item at the given index from the list

# programming languages list
languages = ['Python', 'Java', 'C++', 'French', 'C']

# remove and return the 4th item
return_value = languages.pop(3)
print('Return Value:', return_value)


# updated list
print('Updated list: ', languages)

"""






# e.g.2: pop() without an index, and for negative indices

# programming languages list
languages = ['Python', 'Java', 'C++', 'Ruby', 'C']
languages1 = ['Python', 'Java', 'C++', 'Ruby', 'C']

# remove and return the last item
print('When index is not passed: ')
print('Return Value:', languages.pop())
print('Updated List:', languages)

print(30*'=')

# remove and return the last item
print('\nWhen -1 is passed:')
print('Return Value: ', languages.pop(-1))
print('Updated List:', languages)

print(30*'=')

# remove and return the third item
print('\nWhen -3 is passed"')
print('Return Value: ', languages.pop(-3))
print('Updated List: ', languages)

# remove and return the third last item
print('\nWhen -3 is passed: ')
print('Return Value: ', languages1.pop(-3))
print('Updated List:', languages1)





















