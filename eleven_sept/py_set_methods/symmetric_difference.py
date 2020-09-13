
# python set symmetric_difference() : returns the symmetric difference of sets
# the python symmetric_difference() method returns the symmetric difference of
# 2 sets.

# A.symmetric_difference(B)





"""

# e.g.1: working of symmetric_difference()

A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e'}
C = {}

print(A.symmetric_difference(B))
print(B.symmetric_difference(A))

print(A.symmetric_difference(C))
print(B.symmetric_difference(C))

"""






# Symmetric difference using ^ operator

A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e'}

print(A ^ B)
print(B ^ A)

print(A ^ A)
print(B ^ B)















































