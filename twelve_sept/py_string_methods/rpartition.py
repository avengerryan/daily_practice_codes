
# python string rpartition() : returns a tuple
# the rpartition() splits the string at the last occurrence of the argument
# string and returns a tuple containing the part the before separator, argument
# string and the part after the separator.

# string.rpartition(separator)









# e.g. How rpartition() works

string = "Python is fun"

# 'is' separator is found
print(string.rpartition('is '))

# 'not' separator is not found
print(string.rpartition('not '))

string = "Python is fun, isn't it"

# splits at last occurrence of 'is'
print(string.rpartition('is'))


































