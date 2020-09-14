
# python string translate() : returns mapped charactered string
# the string translate() method returns a string where each character is
# mapped to its corresponding character in the translation table.

# string.translate(table)






"""

# e.g.1: translation/mapping using a translation table with translate()

# first string
firstString = "abc"
secondString = "ghi"
thirdString = "ab"

string = "abcdef"
print("Original string:", string)

translation = string.maketrans(firstString, secondString, thirdString)

# translate string
print("Translated string:", string.translate(translation))

"""








# e.g.2: translation/mapping with translate() with manual translation table

# translation table - a dictionary
translation = {97: None, 98: None, 99: 105}

string = "abcdef"
print("Original string:", string)

# translate string
print("Translated string:", string.translate(translation))


































