
# python string casefold() : converts to case folded string
# the casefold() method is an aggressive lower() method which converts strings ]
# to case folded strings for caseless matching



"""

# e.g.1: lowercase using casefold()

string = "PYTHON IS AWESOME"

# print lowercase string
print("Lowercase string:", string.casefold())

"""






# e.g.2: comparison using casefold

firstString = "def Fluß"
secondString = "der Fluss"


# ß is equivalent to ss
if firstString.casefold() == secondString.casefold():
    print('The strings are equal.')
else:
    print('the string are not equal')



















































