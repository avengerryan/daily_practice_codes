
# Python all()
# the all() method returns True when all elements in the given iterable are true.
# if not, it returns False

# all(iterable)





# example: How all() works for lists

# all values true
l = [1, 3, 4, 5]
print(all(l))


# all values false
l = [0, False]
print(all(l))


# one false value
l = [0, False, 5]
print(all(l))


# empty iterable
l = []
print(all(l))


















