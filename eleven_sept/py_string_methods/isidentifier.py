
# python string isidentifier() : checks for valid identifier
# the isidentifier() method returns True if the string is a valid identifier
# in Python. If not, it returns False


# string.isidentifier()






"""

# e.g.1: how isidentifier() works

str = "Python"
print(str.isidentifier())

str = "Py thon"
print(str.isidentifier())

str = "22Python"
print(str.isidentifier())

str = ''
print(str.isidentifier())

"""









# e.g.2: more e.g. of isidentifier()

str = "root33"
if str.isidentifier() == True:
    print(str, 'is a valid identifier.')
else:
    print(str, 'is not a valid identifier.')

str = "33root"
if str.isidentifier() == True:
    print(str, 'is nto a valid identifier.')
else:
    print(str, 'is not a valid identifier.')

str = "root 33"
if str.isidentifier() == True:
    print(ste, 'is not valid identifier.')
else:
    print(str, 'is not a valid identifier.')












# e.g.1: how isidentifier() works

str = "Python"
print(str.isidentifier())


















