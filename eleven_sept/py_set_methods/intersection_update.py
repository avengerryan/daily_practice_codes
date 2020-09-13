
# Python set intersection_update() : updates calling set with inheritance of sets
# the intersection_update() updates the set calling intersection_update() method
# with the intersection of sets.


"""

# e.g.1: how intersection_update() works

A = {1, 2, 3, 4}
B = {2, 3, 4, 5}

result = A.intersection_update(B)

print('result = ', result)
print('A = ', A)
print('B = ', B)

"""






# e.g.2: intersectio_update() with two parameters

A = {1, 2, 3, 4}
B = {2, 3, 4, 5, 6}
C = {4, 5, 6, 9, 10}

result = C.intersection_update(B, A)

print('result =', result)
print('C =', C)
print('B =', B)
print('A =', A)




























































