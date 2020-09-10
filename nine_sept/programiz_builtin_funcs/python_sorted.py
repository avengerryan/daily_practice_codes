
# python sorted(): returns a sorted list from the given iterable
# the sorted() function returns a sorted list from the items in an iterable

# sorted(iterable, key=None, reverse=False)




"""

# e.g.1: sort string, list, and tuple

# vowels list
py_list = ['e', 'a', 'u', 'o', 'i']
print(sorted(py_list))

# string
py_string = 'Python'
print(sorted(py_string))

# vowels tuple
py_tuple = ('e', 'a', 'u', 'o', 'i')
print(sorted(py_tuple))

"""


"""

# e.g. 2: sort in descending order


# set
py_set = {'e', 'a', 'u', 'o', 'i'}
print(sorted(py_set, reverse=True))

# dictionary
py_dict = {'e': 1, 'a': 2, 'u': 3, 'o': 4, 'i': 5}
print(sorted(py_dict, reverse=True))

# frozen set
frozen_set = frozenset(('e', 'a', 'u', 'o', 'i'))
print(sorted(frozen_set, reverse=True))

"""




# key parameter in Python sorted() function

# sorted(iterable, key=len)


"""

# e.g. 3: sort the list using sorted() having a key function

# take the second element for sort

def take_second(elem):
    return elem[1]


# random list
random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# sort list with key
sorted_list = sorted(random, key=take_second)

# print list
print('Sorted list:', sorted_list)

"""



"""

# Tow tuples can be compared:

print("Tuple comparison: ", (1, 3) > (1, 4))

print("Tuple comparison: ", (1, 4) < (2, 2))

print("Tuple comparison: ", (1, 4, 1) < (2, 1))

"""



# using this above logic, below e.g.
# e.g. 4: sorting with multiple keys

# nested list of student's info in a science olympiad
# list elements: (student's name, marks out of 100, Age)

# participant_list = [
#     ('Alison', 50, 18),
#     ('Terence', 75, 20),
#     ('David', 75, 20),
#     ('Jimmy', 90, 22),
#     ('John', 45, 12)
# ]
#
# def sorter(item):
#     # since highest marks first, least error = most marks
#     error = 100 - item[1]
#     age = item[2]
#     return (error, age)
#
# sorted_list = sorted(participant_list, key=sorter)
# print(sorted_list)




# above program by using lambda function:

participant_list = [
    ('Alison', 50, 18),
    ('Terence', 75, 20),
    ('David', 75, 20),
    ('Jimmy', 90, 22),
    ('John', 45, 12)
]

sorted_list = sorted(participant_list, key=lambda item: (100-item[1], item[2]))
print(sorted_list)






















