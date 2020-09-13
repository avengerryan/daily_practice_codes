
# python string join() : returns a concatenated string
# the join() string method returns a string by joining all the elements of iterable,
# separated by a string separator.

# string.join(iterable)






"""

# e.g.1: working of the join() method

# .join() with lists
numList = ['1', '2', '3', '4']
separator =', '
print(separator.join(numList))

# .join() with tuples
numTuple = ('1', '2', '3', '4')
print(separator.join(numTuple))

s1 = 'abc'
s2 = '123'

# each element of s2 is separated by s1
# '1'+ 'abc'+ '2'+ 'abc'+ '3'
print('s1.join(s2):', s1.join(s2))

# each element of s2 is separated by s2
# '1'+ 'abc'+ '2'+ 'abc'+ '3'
print('s1.join(s2):', s1.join(s2))

# each element of s1 is separated by s2
# 'a'+ '123'+ 'b'+ '123'+ 'b'
print('s2.join(s1):', s2.join(s1))

"""




"""

# e.g.2: the join() method with sets

# join() with sets
test = {'2', '1', '3'}
s = ', '
print(s.join(test))


test = {'Python', 'Java', 'Ruby'}
s = '->->'
print(s.join(test))

"""






# e.g.3: the join() method with dictionaries

# .join() with dictionaries
test = {'mat': 1, 'that': 2}
s = '->'

# joins the keys only
print(s.join(test))

test = {1: 'mat', 2: 'that'}
s = ', '

# this gives error since key isn't string
print(s.join(test))










































































