
# python set issubset() : checks if a set is superset of another set
# the issubset() method returns True if all elements of a set are present
# in another set (passed as an argument). If not, it returns False.





# e.g: how issubset() works

A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {1, 2, 4, 5}


# returns True
print(A.issubset(B))

# returns False
# B is not subset of A
print(B.issubset(A))

# returns False
print(A.issubset(C))

# returns True
print(C.issubset(B))











































