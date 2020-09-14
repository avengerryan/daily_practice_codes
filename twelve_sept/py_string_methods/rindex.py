
# python string rindex() : returns highest index of substring
# the rindex() method returns the highest index of the substring inside
# the string (if found). If the substring is not found, it raises an exception.

# str.rindex(sub[, start[, end]])





"""

# e.g.1: rindex() with no start and end argument

quote = "Let it be, let it be, let it be"

result = quote.rindex('let it')
print("Substring 'let it:", result)

result = quote.rindex('small')
print("Substring 'small ':", result)

"""








# e.g.2: rindex() with start and end arguments

quote = "Do small things with great love"

# substring is searched in ' small things with great love '
print(quote.rindex('t', 2))

# substring is searched in 'll things with'
print(quote.rindex('th', 6, 20))

# substring is searched in 'hings with great lov'
print(quote.rindex('o small ', 10, -1))







































































