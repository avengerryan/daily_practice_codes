
# python string find() : returns the index of first occurrence of substring
# the find() method returns the index of first occurrence of the substring
# (if found). If not found, it returns -1.

# str.find(sub[, start[, end]])





"""

# e.g.1: find() with no start and end argument

quote = "Let it be, let it be, let it be"

# first occurrence of 'let it' (case sensitive)
result = quote.find('let it')
print("Substring 'let it':", result)

# find returns -1 if substring not found
result = quote.find('small')
print("Substring 'small':", result)

# how to use find()
if (quote.find('be,') != -1):
    print("Contains substring 'be,'")
else:
    print("Doesn't contain substring")

"""




# e.g.2: find() with start and end arguments

quote = "Do small things with great love"

# substring is searched in 'hings with great love'
print(quote.find('small things', 10))

# substring is searched in ' small things with great love
print(quote.find('small things', 2))

# substring is searched in 'hings with great lov'
print(quote.find('o small ', 10, -1))

# substring is searched in 'll things with'
print(quote.find('things ', 6, 20))










































