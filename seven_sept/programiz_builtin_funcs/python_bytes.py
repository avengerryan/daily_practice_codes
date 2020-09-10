
# python bytes
# returns immutable bytes object


# the bytes() method returns a immutable bytes object initialized with the given size and data.

# syntax: bytes([source[, encoding[, errors]]])


# convert string to bytes

string = 'Python is interesting.'

# string with encoding 'utf-8'
arr = bytes(string, 'utf-8')
print(arr)

print(30*'=')


# create a byte of given integer size

size = 5

arr = bytes(size)
print(arr)



print(30*'=')



# convert iterable list to bytes

rList = [1, 2, 3, 4, 5]

arr = bytes(rList)
print(arr)



print(30*'=')

















