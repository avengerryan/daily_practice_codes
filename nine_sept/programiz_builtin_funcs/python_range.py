
# Python range() : returns sequence of integers between start and stop
# the range() type returns an immutable sequence of nos. between the given start integer
# to the stop integer


# range(stop)
# range(start, stop[, step])


# r[n] = start + step*n     (for both positive and negative step)
#       where, n >=0 and r[n] < stop (for positive step)
#       where, n >= 0 and r[n] > stop (for negative step)



"""

# e.g 1: how range works in python:

# empty range
print(list(range(0)))

# print(range(0))

print(30*'=')

# using range(stop) = stop - 1
print(list(range(10)))

# print(range(10))

print(30*'=')

# using range(start, stop)
print(list(range(1, 10)))

"""


"""

# e.g 2: create a list of even no. between the given nos. using range()

start = 2
stop = 14
step =2

print(list(range(start, stop, step)))

"""


# e.g. 3: how range() works with negative step

start = 2
stop = -14
step = -2

print(list(range(start, stop, step)))

# value constraint not met
print(list(range(start, 14, step)))































