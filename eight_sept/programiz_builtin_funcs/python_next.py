
# Python next() : retrieves next item from the iterator
# the next() function returns the next item from the iterator


"""

# example 1: get the next item

random = [5, 9, 'cat']

# converting the list to an iterator
random_iterator = iter(random)
print(random_iterator)


print(next(random_iterator))

print(next(random_iterator))

print(next(random_iterator))


# this will raise error
# iterator is exhausted
print(next(random_iterator))


"""



# example 2: passing default value to next()

random = [5, 9]

# converting the list to an iterator
random_iterator = iter(random)

print(next(random_iterator, '-1'))

print(next(random_iterator, '-1'))

# random_iterator is exhausted
print(next(random_iterator, '-1'))
print(next(random_iterator, '-1'))
print(next(random_iterator, '-1'))




























