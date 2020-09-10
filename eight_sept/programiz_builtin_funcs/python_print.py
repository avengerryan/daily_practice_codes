
# python print() : prints the given object.
# the print() function prints the given object to the standard output device (screen)
# or to the text stream file.


"""

# example 1: how print() works in python

# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

print("Python is fun.")

a = 5
# two objects are passed
print("a =", a)

b = a
# three objects are passed
print('a =', a, ' = b')

"""


"""

# example 2: print() with separator and end parameter

a = 5
print("a =", a, sep='00000', end='\n\n\n')
print("a =", a, sep='0', end='')

"""




# example 3: print() with file parameter


sourceFile = open('python.txt', 'w')
print('Pretty cool, huh!', file = sourceFile)
sourceFile.close()

# check the respective code folder, u will find a python.txt file created there.































