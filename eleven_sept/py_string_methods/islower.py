
# python string islower() : checks if all alphabets in a string are lowercase.
# the islower() method returns True if all alphabets i a string are lowercase alphabets.
# If the string contains at least one uppercase alphabet, it returns False.


# string.islower()







"""

# e.g.1: return value from islower()

s = "this is good"
print(s.islower())

s = 'th!s is also g00d'
print(s.islower())

s = 'this is Not good'
print(s.islower())

"""







# e.g.2: how to use islower() in a program

s = 'this is good'
if s.islower() == True:
    print("Does not contain uppercase letter.")
else:
    print("Contains uppercase letter.")

s = 'this is Good'
if s.islower() == True:
    print("Does not contain uppercase letter.")
else:
    print("Contains uppercase letter.")



























