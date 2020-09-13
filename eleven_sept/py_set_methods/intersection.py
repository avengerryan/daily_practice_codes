
# python set intersection() : returns intersection of 2 or more sets
# the intersection() method returns a new set with elements that are common
# to all sets






"""

# e.g.1: how intersection() works

A = {2, 3, 5, 4}
B = {2, 5, 100}
C = {2, 3, 8, 9, 10}

print(B.intersection(A))
print(B.intersection(C))
print(A.intersection(C))
print(C.intersection(A, B))

"""




"""

# e.g.2:
0
A = {100, 7, 8}
B = {200, 4, 5}
C = {300, 2, 3}
D = {100, 200, 300}

print(A.intersection(D))
print(B.intersection(D))
print(C.intersection(D))
print(A.intersection(B, C, D))

"""





# e.g.3: set intersection using and operator

A = {100, 7, 8}
B = {200, 4, 5}
C = {300, 2, 3, 7}
D = {100, 200, 300}


print(A & C)
print(A & D)

print(A & C & D)
print(A & B & C & D)








































































