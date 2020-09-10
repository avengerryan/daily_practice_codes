
# Python exec()
# Executes dynamically created program.

# the exec() method executes the dynamically created program, which is either
# a string or a code object.

# example: how exec() works

"""
a = 5\n
b = 10\n
print("Sum =", a + b)

"""


"""
program = 'a = 5\nb=10\nprint("Sum =", a+b)'
exec(program)

"""


"""
# example: Allow user to provide input

program = input('enter a program: ')
exec(program)

# Type this after running the program: [print(item) for item in [1,2,3]]


# if you want to take python code from the user which allows multiline code (using '\n')
# you can use compile() method before using exec()

"""


"""
# we can use dir() method to see which variable and methods the user can have access to

from math import *
exec('print(dir())')

"""


"""

# Passing empty dictionary as globals parameter

from math import *
exec('print(dir())', {})

# this code will raise an exception
# exec('print(sqrt(9))', {})

"""


"""

# Making certain methods available

from math import *
exec('print(dir())', {'sqrt': sqrt, 'pow': pow})

# object can have sqrt() module
exec('print(sqrt(9))', {'sqrt': sqrt, 'pow': pow})

"""

"""
from math import *
exec('print(dir())', {'squareRoot': sqrt, 'pow': pow})

# object can have squareRoot() module
exec('print(squareRoot(9))', {'squareRoot': sqrt, 'pow': pow})

"""


# we can restrict the use of __builtins__ by giving value None to the '__builtins__'
# in the globals dictionary



# Passing both globals and locals dictionary

from math import *

globalsParameter = {'__builtins__': None}
localsParameter = {'print': print, 'dir': dir}
exec('print(dir())', globalsParameter, localsParameter)











