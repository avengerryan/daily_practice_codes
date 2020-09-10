
# Python str() : returns the string version of the object.
# the str() function returns the string version of the given object


# str(object, encoding='utf-8', errors='strict')


"""

# e.g.1: convert to string

result = str(10)
print(result)

# value 10 is present there as a string in the result variable, bcoz of str
# print(type(result))

"""




# e.g. 2: how str() works for bytes

# bytes
b = bytes('pythön', encoding='utf-8')

print(str(b, encoding='ascii', errors='ignore'))

# Here, the character 'ö' cannot be decoded by ASCII.
# set the errors ='ignore' to ignore the error before hand, due to this.































