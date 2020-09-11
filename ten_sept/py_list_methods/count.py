
# python list count(): returns count of the element in the list
# the count() method returns the no. of times the specified element appears in the list

# list.count(element)


"""

# e.g. 1: use of count()

# vowels list
vowels = ['a', 'e', 'i', 'o', 'i', 'u']

# count element 'i'
count = vowels.count('i')

# print count
print('The count of i is: ', count)

# count element 'p'
count = vowels.count('p')

# print count
print('The count of p is: ', count)

"""




# e.g. 2: count tuple and list elements inside list

# random list
random = ['a', ('a', 'b'), ('a', 'b'), [3, 4]]

# count element ('a', 'b')
count = random.count(('a', 'b'))

# print count
print("The count of ('a', 'b') is ", count)

# count element [3, 4]
count = random.count([3, 4])

# print count
print("the count of [3, 4] is: ", count)