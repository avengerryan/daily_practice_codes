
# Python Dictionary pop() : removes and returns element having given key.
# the pop() method removes and returns an element from a dictionary having the
# given key.

# dictionary.pop(key[, default])



"""

# e.g.1: pop an element from the dictionary

# random sales dictionary
sales = {'apple': 2, 'orange': 3, 'grapes': 4}

element = sales.pop('apple')
print('The popped element is: ', element)
print('The dictionary is: ', sales)

"""




"""

# e.g. 2: pop an element not present from the dictionary

# random sales dictionary
sales = {'apple': 2, 'orange': 3, 'grapes': 4}

element = sales.pop('guava')

# as guava is not present, we will get KeyError
print(element)

"""





# e.g. 3: pop an element not present from the dictionary, provided a default value.

# random sales dictionary
sales = {'apple': 2, 'orange': 3, 'grapes': 4}

element = sales.pop('guava', 'banana')
print('The popped element is: ', element)
print('The dictionary is: ', sales)











