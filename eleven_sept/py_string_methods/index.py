
# python string index() : returns index of substring
# the index() method returns the index of a substring inside the string (if found)
# If the substring is not found, it raises an exception.

# str.index(sub[, start[, end]])




"""

# e.g.1: index() with substring argument only

sentence = "Python programming is fun."

result = sentence.index("is fun")
print("Substring 'is fun': ", result)

result = sentence.index('Java')
print("Substring 'Java': ", result)

"""







# e.g.2: index() with start and end arguments

sentence = "Python programming is fun."

# substring is searched in 'gramming is fun.'
print(sentence.index('ing', 10))

# substring is searched in'gramming is '
print(sentence.index('g is', 10, -4))

# substring is searched in 'programming'
print(sentence.index('fun', 7, 18))