
# python ascii()

# ascii() method returns a string containing a printable representation
# of an object.
# python ascii() escapes the non-ASCII characters in the string using \x, \u, and \U escapes.

# ascii() returns a string containing a printable represnetation of an object.

# the non-ascii characters in the string are escaped using \x, \u, or \U

# For example, ö is changed to \xf6n, √ is changed to \u221a
# The non-ASCII characters in the string are escaped using \x, \u or \U.


# this below normalText is in camel case
normalText = 'Python is interesting'
print(ascii(normalText))

otherText = 'Pythön is interesting'
print(ascii(otherText))

print('Pyth\xf6n is interesting')



print("="*50)
print('\n')


randomList = ['Python', 'Python', 5]
print(ascii(randomList))