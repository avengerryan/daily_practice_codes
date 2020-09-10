
# python globals()
# returns dictionary of current global symbol table

# the globals() method returns the dictionary of the current global system table


"""
# Example: how globals() method works in python

print(globals())

# raw = globals()
# print(raw)

"""



# example: modify global variable using globals()

age = 23
print(globals())

print(30*'=')

globals()['age'] = 25
print('the age is:', age)










