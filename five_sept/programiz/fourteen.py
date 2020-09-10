
# transpose a matrix

# transpose of a matrix is the interchanging of rows and columns.


X = [[12, 7],
     [4, 5],
     [3, 8]]

result = [[0, 0, 0],
          [0, 0, 0]]


# iterate through rows
for i in range(len(X)):
    # iterate through columns
    for j in range(len(X[0])):
        result[j][i] = X[i][j]

for r in result:
    print('Result: ', r)















