
# python string maketrans() : returns a translation table
# the string maketrans() method returns a mapping table for transaction usable
# for translate() method

# string.maketrans(x[, y[, z]])





"""

# e.g.1: translation table using a dictionary with maketrans()

# e.g. dictionary
dict = {'a': '123', 'b': '456', 'c': '789'}
string = 'abc'
print(string.maketrans(dict))


# e.g. dictionary
dict = {97: '123', 98: '456', 99: '789'}
string = 'abc'
print(string.maketrans(dict))

"""





"""

# e.g.2: translation table using 2 strings with maketrans()

# first string
firstString = "abc"
secondString = "def"
string = "abc"
print(string.maketrans(firstString, secondString))


# example dictionary
firstString = 'abc'
secondString = 'defghi'
string = "abc"
print(string.maketrans(firstString, secondString))

"""







# e.g.3: translational table with removable string with maketrans()

# first string
firstString = "abc"
secondString = "def"
thirdString = "abd"
string = "abc"
print(string.maketrans(firstString, secondString, thirdString))

















































