
# python string isalpha() : checks if all characters are alphabets
# the isalpha() method returns True if all characters in the string are alphabets.
# if not, it returns False.

# string.isalpha()






# e.g.1: working of isalpha()

name = "Monica"
print(name.isalpha())

# contains whitespace
name = "Monica Geller"
print(name.isalpha())

# contains number
name = "Mo3nicaGell22er"
print(name.isalpha())

# e.g.1: working of isalpha()

name = "MonicaGeller"

if name.isalpha() == True:
    print("All characters are alphabets")
else:
    print("All characters are not alphabets.")






























