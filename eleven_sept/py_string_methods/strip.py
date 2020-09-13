
# python string strip() : removes both leading and trailing characters
# the strip() method returns a copy of the string by removing both the leading
# and the trailing characters (based on the string argument passed).

# string.strip([chars])








# e.g. working of the strip() method

string = '  x0x0 love xoxo'

# leading and trailing whitespaces are removed
print(string.strip())

# all <whitespace>,x,o,e characters in the left and right of the string are removed
print(string.strip('    xoe'))

# argument doesn't contain space. No characters are removed
print(string.strip('stx'))

string = 'android is awesome'
print(string.strip('an'))































































