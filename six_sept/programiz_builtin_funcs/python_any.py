
# Python any()
# the any() function returns True if any element of an iterable is True.
# if not, any() returns False.



# example: using any() on Python lists

# True since 1, 3 and 4 (at least one) is true
l = [1, 3, 4, 0]
print(any(l))

# False since both are false
l = [0, False]
print(any(l))

# True since 5 is true
l = [0, False, 5]
print(any(l))

# False since iterable is empty
l = []
print(any(l))




# example 2: using any() on python string

# atleast one (in fact all) elements are True
s = "This is good"
print(any(s))

# 0 is False
# '0' is True since its a string character
s = '000'
print(any(s))

# False since empty iterable
s = ''
print(any(s))

print("==============================================================================")


# Using any() with python dictionaries


# 0 is False
d = {0: 'False'}
print(any(d))

# 1 is True
d = {0: "False", 1: 'True'}

# 0 and False are False
d = {0: 'False', False: 0}
print(any(d))

# iterable is empty
d = {}
print(any(d))

# 0 is False
# '0' is True
d = {'0': False}
print(any(d))




































