
# python string expandtabs() : replaces tab character with spaces
# the expandtabs() method returns a copy of string with all tab characters '\t'
# replaced with whitespace characters until the next multiple of tabsize parameter.

# string.expandtabs(tabsize)




"""

# e.g.1: expandtabs() with no argument

str = 'xyz\t12345\tabc'

# no argument is passed
# default tabsize is 8
result = str.expandtabs()

print(result)

"""








# e.g.2: expandtabs() with different argument

str = "xyz\t12345\tabc"
print('Original String: ', str)

# tabsize is set to 2
print('Tabsize 2:', str.expandtabs(2))

# tabsize is set to 3:
print('Tabsize 3:', str.expandtabs(3))

# tabsize is set to 4:
print('Tabsize 4:', str.expandtabs(4))

# tabsize is set to 5:
print('Tabsize 5:', str.expandtabs(5))

# tabsize is set to 6:
print('Tabsize 6:', str.expandtabs(6))
























