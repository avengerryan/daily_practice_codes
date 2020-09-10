
# Python __import__() : Function called by the import statement.
# the __import__() is a function that is called by the import statement.


# __import__(name, globals=None, locals=None, fromList=(), level=0)






# e.g.: how __import__() works

mathematics = __import__('math', globals(), locals(), [], 0)
print(mathematics.fabs(-2.5))



import math
math.fabs(x)



mathematics.fabs(x)




















