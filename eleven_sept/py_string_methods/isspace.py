
# python string isspace() : Checks whitespace characters.
# The  isspace() method returns True if there are only whitespace characters in the
# string. If not, it returns False

# string.isspace()





"""

# e.g.1: working of isspace()

s = '   \t'
print(s.isspace())

s = ' a '
print(s.isspace())

s = ''
print(s.isspace())

"""







# e.g.2: how to use isspace()

s = '\t \n'
if s.isspace() == True:
    print("All whitespace characters")
else:
    print("Contains non-whitespace characters")

s = '2+2 = 4'

if s.isspace() == True:
    print("All whitespace characters")
else:
    print("Contains non-whitespace characters.")























































