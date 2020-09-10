
# Python set() : constructs and returns a set.
# the set() built in creates a set in python


"""

# e.g. 1: create sets from string, tuple, list, and range

# empty set
print(set())

# from string
print(set('Python'))

# from tuple
print(set(('a', 'e', 'i', 'o', 'u')))

# from list
print(set(['a', 'e', 'i', 'o', 'u']))

# from range
print(set(range(5)))

"""


"""

# e.g. 2: create sets from another set, dictionary and frozen set

# from set
print(set({'a', 'e', 'i', 'o', 'u'}))

# from dictionary
print(set({'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}))

# from frozen set
frozen_set = frozenset(('a', 'e', 'i', 'o', 'u'))
print(set(frozen_set))


"""



# e.g.3: create set() for a custom iterable object

class PrintNumber:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if(self.num >= self.max):
            raise StopIteration
        self.num += 1
        return self.num

# print_num is an iterable
print_num = PrintNumber(5)

# creating a set
print(set(print_num))




























