
# python set frozenset() : returns immutable frozenset object
# the frozenset() function returns an immutable frozenset object initialized with
# elements from the given iterable.





"""

# e.g.1: working of python frozenset()

# tuple of vowels
vowels = ('a', 'e', 'i', 'o', 'u')

fSet = frozenset(vowels)
print('the frozen set is:', fSet)
print('the empty frozen set is:', frozenset())


# frozensets are immutable
fSet.add('v')

"""




"""

# e.g.2: frozenset() for dictionary

# random dictionary
person = {'name': 'John', 'age': 23, 'sex': 'male'}

fSet = frozenset(person)
print('the frozen set is:', fSet)

"""




# Frozenset operations


"""

# frozensets
# initialize A and B
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])

# copying a frozenset
C = A.copy()
print(C)

# union
print(A.union(B))

# intersection
print(A.intersection(B))

# difference
print(A.difference(B))

# symmetric_difference
print(A.symmetric_difference(B))

"""





# frozensets
# initialize A, B, and C
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])
C = frozenset([5, 6])

# isdisjoint() method
print(A.isdisjoint(C))

# issubset() method
print(C.issubset(B))

# issuperset() method
print(B.issuperset(C))




































































