
# add 2 matrices


# In python we can implement a matrix as a nested list.
# we can treat each element as a row of the matrix

# example: x = [[1, 2], [4, 5], [3, 6]]
# this represents a 3x2 matrix. First row can be selected as x[0] and the element
# in the first row, first column can be selected as x[0][0]

X = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

Y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]

result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]


# iterate through rows
for i in range(len(X)):
    # iterate through columns
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]

for r in result:
    print(r)





