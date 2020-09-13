
# python string isprintable() : checks printable character
# the isprintable() methods returns True if all character in the string are printable
# or the string is empty. If not, it returns False.

# string.isprintable()







"""

# e.g.1: working of isprintable()

s = "space is a printable"
print(s)
print(s.isnumeric())

s = "\nNew Line is printable"
print(s)
print(s.isprintable())

s = ''
print("\nEmpty string printable?", s.isprintable())

"""








# e.g.2: how to use isprintable()

# written using ASCII
# chr(27) is escape character
# char(97) is letter 'a'


s = chr(27) + chr(97)

if s.isprintable() == True:
    print("Printable")

else:
    print("Not Printable")

s = '2+2 = 4'

if s.isprintable() == True:
    print("Printable")
else:
    print("Non Printable")























