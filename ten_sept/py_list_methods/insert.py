
# python list insert() : insert an element to the list
# the list insert() method inserts an element to the list at the specified index

# list.insert(i, elem)



"""

# e.g. 1: inserting an element to the list

# vowel list
vowel = ['a', 'e', 'i', 'u']

# 'o' is inserted at index 3
# the position of 'o' will be 4th
vowel.insert(3, 'o')

print('Updated List: ', vowel)

"""




# e.g. 2: Inserting a tuple (as an element) to the list

mixed_list = [{1, 2}, [5, 6, 7]]

# number tuple
number_tuple = (3, 4)

# inserting a tuple to the list
mixed_list.insert(1, number_tuple)

print('Updated List: ', mixed_list)

