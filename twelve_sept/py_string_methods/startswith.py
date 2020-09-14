
# python string startswith() : checks if string starts with the specified string
# the startswith() method returns True if a string starts with the specified
# prefix(string). If not, it returns False

# str.startswith(prefix[, start[, end]])









"""

# e.g.1: startswith() without start and end parameters

text = "Python is easy to learn."

result = text.startswith('is easy')
# returns False
print(result)

result = text.startswith("Python is")
print(result)

result = text.startswith("Python is easy to learn.")
# returns True
print(result)

"""






"""

# e.g.2: startswith() with start and end parameters

text = "Python programming is easy."

# start parameter: 7
# 'programming is easy.' string is searched
result = text.startswith('programming is', 7)
print(result)


# start: 7, end: 18
# 'programming' string is searched
result = text.startswith('programming is', 7, 18)
print(result)

result = text.startswith('program', 7, 18)
print(result)

"""











# passing Tuple to startswith() :

# e.g.3: startswith() with Tuple Prefix

text = "programming is easy"
result = text.startswith(('python', 'programming'))

# prints True
print(result)

result = text.startswith(('is', 'easy', 'java'))

# prints False
print(result)

# with start and end parameter
# 'is easy' string is checked
result = text.startswith(('programming', 'easy'), 12, 19)

# prints False
print(result)



















































