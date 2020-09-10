
# Python dictionary items() : returns view of dictionary's (key, value) pair.
# The items() method returns a view object that displays a list dictionary's (key, value_ tuple pairs.


"""

# e.g. 1: get all items of a dictionary with items

# random sales dictionary
sales = {'apple': 2, 'orange': 3, 'grapes': 4}

print(sales.items())

"""






# e.g. 2: how items() works when a dictionary is modified

# random sales dictionary
sales = {'apples': 2, 'orange': 3, 'grapes': 4}

items = sales.items()
print('Original items: ', items)

# delete an item from dictionary
del[sales['apple']]
print('Updated items:', items)

















