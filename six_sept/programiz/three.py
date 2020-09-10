
# count the number of each vowel

# using a list and a dictionary comprehension


ip_str = 'Hello, have you tried our tutorial section yet?'

# make it suitable for caseless comparisons
ip_str = ip_str.casefold()

# count the vowels
count = {x:sum([1 for char in ip_str if char == x]) for x in 'aeiou'}

print(count)



























