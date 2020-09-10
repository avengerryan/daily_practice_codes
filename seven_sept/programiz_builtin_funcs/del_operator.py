
# after learning delattr, we will use del operator to delet class attributes


class Coordinate:
    x = 10
    y = -5
    z = 0

point1 = Coordinate()

print('x = ', point1.x)
print('y = ', point1.y)
print('z = ', point1.z)


# deleting attribute z
del Coordinate.z

print('--After deleting z attribute--')
print('x = ', point1.x)
print('y = ', point1.y)

# raises attribute error
print('z = ', point1.z)