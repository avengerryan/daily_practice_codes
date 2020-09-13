
# python list copy() : returns a shallow copy of a list
# the copy() method returns a shallow copy of the list

# new_list = list.copy()



"""

# using = operator

old_list = [1, 2, 3]
new_list = old_list

print(old_list)

print(new_list)

"""



"""

# NOTE:

old_list = [1, 2, 3]
new_list = old_list

# add an element to the list and the copied list also changes
new_list.append('a')

print('New List: ', new_list)
print('Old List: ', old_list)

"""




"""

# copy() doesn't modify the old list

# e.g.1 Copying a list

# mixed list
my_list = ['cat', 0, 6, 7]

# copying a list
new_list = my_list.copy()

print('Copied List: ', new_list)

"""




"""

# e.g.2 Copy list using slicing syntax

# shallow copy using the slicing syntax

# mixed list
list = ['cat', 0, 6.7]

# copying a list using slicing
new_list = list[:]

# adding an element to the new list
new_list.append('dog')

# printing new and old list
print('Old List: ', list)
print('New List: ', new_list)

"""












































