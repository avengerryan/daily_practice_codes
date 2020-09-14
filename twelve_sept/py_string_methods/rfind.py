
# python string rfind() : returns the highest index of substring
# the rfind() method returns the highest index of the substring (if found)
# If not found, it returns -1

# str.rfing(sub[, start[, end]])





"""

# e.g.1: rfind() with No start and end Argument

quote = 'Let it be, let it be, let it be'

result = quote.rfind('let it')
print("Substring 'let it' :", result)

result = quote.rfind('small')
print("substring 'small':", result)

result = quote.rfind('small')
if (result != -1):
    print("Highest index where 'be,' occurs:", result)
else:
    print("Doesn't contains substring")

"""








# e.g.2: rfind() with start and end arguments

quote = "Do small things with great love"

# substring is searched in 'hings with great love'
print(quote.rfind('things', 10))

# substring is searched in ' small things with great love'
print(quote.rfind('t', 2))

# substring is searched in 'hings with great lov'
print(quote.rfind('o small ', 10, -1))

# substring is searched in 'll things with'
print(quote.rfind('th', 6, 20))





































