
# python string rstrip() : removes trailing characters.
# the rstrip() method returns a copy of the string with trailing characters
# removed (based on the string argument passed)

# string.rstrip([chars])






# e.g. working of rstrip()

random_string = ' this is good'

# leading whitespace are removed
print(random_string.rstrip())

# argument doesn't contain 'd'
# no characters are removed
print(random_string.rstrip('so oo'))

print(random_string.rstrip('sid oo'))

website = 'www.programiz.com/'
print(website.rstrip('m/.'))















































