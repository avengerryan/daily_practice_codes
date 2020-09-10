
# Operations like copy, difference, intersection, symmetric_difference and union

# frozensets
# initialize A and B

"""
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





# for isdisjoint, issubset, and issuperset

# initialize A, B, and C

A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])
C = frozenset([5, 6])

# isdisjoint() method
print(A.isdisjoint(C))

# issubset()
print(C.issubset(B))

# issuperset()
print(B.issuperset(C))








