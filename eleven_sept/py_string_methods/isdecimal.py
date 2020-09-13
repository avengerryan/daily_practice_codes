
# python string isdecimal() : checks decimal characters
# the isdecimal() method returns True if all characters in a string are decimal
# characters. If not, it returns False.

# string.isdecimal()



"""

# e.g.1: working of isdecimal()

s = "28212"
print(s.isdecimal())

# contains alphabets
s = "32ladk3"
print(s.isdecimal())

# contains alphabets and spaces
s = "Mo2 nicaG el 122er"
print(s.isdecimal())

"""






# e.g.2: string containing digits and numeric characters

s = "23455"
print(s.isdecimal())

# s = '3455'
s = '\u00B23455'
print(s.isdecimal())

# s = '1/2'
s = '\u00BD'
print(s.isdecimal())


















































