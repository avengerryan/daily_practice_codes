
# python string isalnum() : checks alphanumeric character
# the isalnum() method returns True if all characters in the string are alphanumeric (either
# alphabets or numbers). If not, it returns False.


# string.isalnum()





"""

# e.g.1: working of isalnum()

name = "M234onica"
print(name.isalnum())

# contains whitespace
name = "M3onica Gell22er"
print(name.isalnum())

name = "Mo3nicaGell22er"
print(name.isalnum())

name = "133"
print(name.isalnum())

"""





# e.g.1: working of isalnum()

name = "Mon1caG3ll3r"

if name.isalnum() == True:
    print("All characters of string (name) are alphanumeric.")
else:
    print("All characters are not alphanumeric.")














