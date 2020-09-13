
# python string count() : returns occurrences of substring in string.
# the string count() method returns the no. of occurrences of a
# substring in the given string.

# string.count(substring, start=..., end=...)




"""

# e.g.1: count number of occurrences of a given substring

# define string
string = "Python is awesome, isn't it?"
substring = "is"

count = string.count(substring)

# print count
print("The count is:", count)

"""





# e.g.2: count number of occurrences of a given substring using start and end

# define string
string = "Python is awesome, isn't it?"
substring = "i"

# count after first 'i' and before the last 'i'
count = string.count(substring, 8, 25)

# print count
print("The count is:", count)











































