
# python string format() : formats string into nicer output
# the sting format() method formats the given string into a nicer output in python

# template.format(p0, p1, ....., k0=v0, k1=v1, ....)





"""

# e.g.1: basic formatting for default, positional and keyword arguments

# default arguments
print("Hello {}, your balance is {}.".format("Adam", 230.2346))

# positional argument
print("Hello {0}, your balance is {1}.".format("Adam", 230.2346))

# keyword arguments
print("Hello {name}, your balance is {blc}.".format(name="Adam", blc=230.2346))

# mixed arguments
print("Hello {0}, your balance is {blc}.".format("Adam", blc=230.2346))

"""





"""

# e.g.3: number formatting with padding for int and floats

# integer numbers with minimum width
print("{:5d}".format(12))

# width doesn't work for numbers longer than padding
print("{:2d}".format(1234))

# padding for float numbers
print("{:8.3f}".format(12.2346))

# integer numbers with minimum width filled with zeros
print("{:05d}".format(12))

# padding for float numbers filled with zeros
print("{:08.3f}".format(12.2346))

"""





"""

# e.g.4: Number formatting for signed numbers

# show the + sign
print("{:+f} {:+f}".format(12.23, -12.23))

# show the - sign only
print("{:-f} {:-f}".format(12.3, -12.23))

# show space for + sign
print("{: f} {: f}".format(12.23, -12.23))

"""





"""

# e.g.5: number formatting with left, right and center alignment

# integer numbers with right alignment
print("{:5d}".format(12))

# float numbers with center alignment
print("{:^10.3f}".format(12.2346))

# integer left alignment filled with zeros
print("{:<05d}".format(12))

# float numbers with center alignment
print("{:=8.3f}".format(-12.2346))

"""




"""

# string formatting with format()

# e.g.6: string formatting with padding and alignment

# string padding with left alignment
print("{:5}".format("cat"))

# string padding with right alignment
print("{:>5}".format("cat"))

# string padding with center alignment
print("{:^5}".format("cat"))

# string padding with center alignment
# and '*' padding character
print("{:*^5}".format("cat"))

"""







"""

# e.g.7 Truncating strings with format()

# truncating strings to 3 letters
print("{:.3}".format("caterpillar"))

# truncating strings to 3 letters and padding
print("{:5.3}".format("caterpillar"))

# truncating strings to 3 letter, padding and center alignment
print("{:^5.3}".format("caterpillar"))

"""






# Formatting class and dictionary members using format()


"""

# e.g.8: formatting class members using format()

# define Person class

class Person:
    age = 23
    name = "Adam"

# format age
print("{p.name}'s age is: {p.age}".format(p=Person()))

"""






"""

# e.g.9: formatting dictionary members using format()

# define Person dictionary
person = {'age': 23, 'name': 'Adam'}

# format age
print("{p[name]}'s age is: {p[age]}".format(p=person))

"""

"""
# Another way to do above e.g. is

# define Person dictionary
person = {'age': 23, 'name': 'Adam'}

# format age
print("{name}'s age is: {age}".format(**person))

"""










# Arguments as format codes using format()

"""

# e.g.10: dynamic formatting using format()

# dynamic string format template
string = "{:{fill}{align}{width}}"

# passing format codes as arguments
print(string.format('cat', fill='*', align='^', width=5))

# dynamic float format template
num = "{:{align}{width}.{precision}f}"

# passing format codes as arguments
print(num.format(123.236, align=))

"""








"""

# Extra formatting options with format()

# e.g.11: type-specific formatting with format() and overriding __format__() method

import datetime

# datetime formatting
date = datetime.datetime.now()
print("It's now: {:%Y/%m/%d %H:%M:%S}".format(date))

# complex no. formatting
complexNumber = 1+2j
print("Real part: {0.real} and Imaginary part: {0.imag}".format(complexNumber))

# custom __format__() method
class Person:
    def __format__(self, format):
        if(format == 'age'):
            return '23'
        return 'None'

print("Adams's age is: {:age}".format(Person()))

"""






# e.g.12: __str__() and __repr__() shorthand !r and !s using format()

# __str__() and __repr__() shorthand !r and !s
print("Quotes: {0!r}, Without Quotes: {0!s}".format("cat"))

# __str__() and __repr__() implementation !r and !s
class Person:
    def __str__(self):
        return "STR"

    def __repr__(self):
        return "REPR"

print("repr: {p!r}, str: {p!s}".format(p=Person()))




























