
# python string encode() : returns encoded string of given string
# the string encode() method returns encoded version of the given string

# string.encode(encoding='UTF-8', errors='strict')



"""

# e.g.1: encode to default Utf-8 encoding

# unicode string
string = "pythön!"

# print string
print("The string is:", string)

# default encoding to utf-8
string_utf = string.encode()

# print result
print("The encoded version is:", string_utf)

"""






# e.g.1: encoding with error parameter

string = "pythön!"

# print string
print("The string is:", string)

# ignore error
print("The encoded version (with ignore) is:", string.encode("ascii", "ignore"))

# replace error
print("The encoded version (with replace) is:", string.encode("ascii", "replace"))





















