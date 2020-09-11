
# Python Dictionary values() : returns view of all values in dictionary.
# the values() method returns a view object that displays a list of all the values
# in the dictionary.

# dictionary.values()



"""

# e.g. 1: get all values from the dictionary.

# random sales dictionary
sales = {'apple': 2, 'orange': 3, 'grapes': 4}

print(sales.values())

"""





# e.g. 2: how values() works when dictionary is modified

# random sales dictionary
sales = {'apple': 2, 'orange': 3, 'grapes': 4}

values = sales.values()
print('Original items: ', values)

# delete an item from dictionary
del[sales['apple']]
print('Updated items:', values)





















