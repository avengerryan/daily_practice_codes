
# python compile: returns a python code object
# the compile() method returns a python code object from the source (normal string, a byte, or an AST object).

# syntax: compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)
# compile() method is used if the python code is in string form or is an AST object, and you
# want to change it to a code object.

# compile() method returns a python code object


codeInString = 'a = 5\nb=6\nsum=a+b\nprint("sum =", sum)'
codeObject = compile(codeInString, 'sumstring', 'exec')

exec(codeObject)





















