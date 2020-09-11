
# python list extend() : adds iterable elements to the end of the list
# the extend() method adds all the elements of an iterable (list, tuple,
# string etc) to the end of the list.

# list.extend(iterable)



"""

# e.g. 1: using extend() method

# language list
language = ['French', 'English']

# another list of language
language1 = ['Spanish', 'Portuguese']

# appending language1 elements to language
language.extend(language1)

print('Language List: ', language)

"""



"""

# e.g. 2: Add elements of tuple and set to list

# language list
language = ['French']

# language tuple
language_tuple = ('Spanish', 'Portuguese')

# language set
language_set = {'Chinese', 'Japanese'}

# appending language_tuple elements to language
language.extend(language_tuple)

print('New Language List: ', language)

# appending language_set elements to language
language.extend(language_set)

print('Newer Language List: ', language)

"""




"""

# other ways to extend list

# 1. the + operator

a = [1, 2]
b = [3, 4]

a += b

print('a = ', a)

"""



"""

# 2. the list slicing syntax

a = [1, 2]
b = [3, 4]

a[len(a):] = b

print('a = ', a)

"""



# Python extend() vs append()

a1 = [1, 2]
a2 = [1, 2]
b = (3, 4)

a1.extend(b)
print(a1)

a2.append(b)
print(a2)































