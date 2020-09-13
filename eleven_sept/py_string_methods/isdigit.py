
# python string isdigit() : checks digit characters
# the isdigit() method returns True if all character in a string are digits.
# if not, it returns False

# string.isdigit()






"""

# e.g.1: working of isdigit()

s = "28212"
print(s.isdigit())

# contains alphabets and spaces
s = "Mo3 nicaG el 122er"
print(s.isdigit())

"""






# e.g.2: string containing digits and numeric characters

s = '23455'
print(s.isdigit())

# s = '23455'
# subscript is a digit
s = '\u00B23455'
print(s.isdigit())

# s '1/2'
# fraction is not a digit
s = '\u00BD'
print(s.isdigit())























