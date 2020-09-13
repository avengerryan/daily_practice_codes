
# python string isnumeric() : checks numeric characters
# the isnumeric() method returns True if all caharacters in a string are numeric
# characters. If not, it returns False


# string.isnumeric()





"""

# e.g.1: working of isnumeric()

s = "1242323"
print(s.isnumeric())

# s = '23455'
s = '\u00B23455'
print(s.isnumeric())

# s = '1/2'
s = '\u00BD'
print(s.isnumeric())

s = '1242323'
s = 'python12'
print(s.isnumeric())

"""









# e.g.2: how to use isnumeric()

# s = '23455'
s = '\u00B23455'

if s.isnumeric() == True:
    print("All characters are numeric.")
else:
    print("All characters are not numeric.")





























