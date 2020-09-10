
# Python bytearray()
# returns array of given byte size
# it returns a bytearay object which is an array of the given bytes.

# syntax: bytearray([source[, encoding[, errors]]])


# bytearray() method returns a bytearray object which is mutable sequence of integers in the range 0 <= x < 256


string = "Python is interesting."

# string withe encoding 'utf-8'
arr = bytearray(string,'utf-8')
print(arr)


print(30*'=')

size = 5

arr = bytearray(size)
print(arr)


print(30*'=')

rList = [1, 2, 3, 4, 5]

arr = bytearray(rList)
print(arr)



















