
# python string endswith() : checks if string ends with the specified suffix
# the endswith() method returns True if a string ends with the specified suffix.
# if not, it returns False

# str.endswith(suffix[, start[, end])




"""

# e.g.1: endswith() without start and end parameters

text = "Python is easy to learn."

# returns False, due to missing fullstop
result = text.endswith('to learn')

print(result)


result = text.endswith('to learn.')
print(result)

result = text.endswith('Python is easy to learn.')

# returns True
print(result)

"""




"""

# e.g.2: endswith() with start and end parameters

text = "Python programming is easy to learn."

# start parameter: 7
# "programming is easy to learn." string is searched
result = text.endswith('learn.', 7)
print(result)

# both start and end is provided
# start: 7, end: 26
# "programming is easy" string is searched

result = text.endswith('is', 7, 26)
# returns False
print(result)

result = text.endswith('easy', 7, 26)
# returns True
print(result)

"""






# e.g.3: endswith() with tuple suffix

text = "programming is easy"
result = text.endswith(('programming', 'python'))

# prints False
print(result)

result = text.endswith(('python', 'easy', 'java'))
# prints True
print(result)

# with start and end parameter
# 'programming is' string is checked
result = text.endswith(('is', 'an'), 0, 14)

# prints True
print(result)






















