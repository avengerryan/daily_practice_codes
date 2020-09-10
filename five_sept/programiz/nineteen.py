
# to remove punctuations from a string


# if we want to break a sentence into a list of words

# first we have to clean up the string and remove all punctuation marks.


# define punctuations
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

my_str = 'Hello!!!, he said ---and went.'

# to take input from the user
# my_str = input("Enter a string: ")

# remove punctuation from the string

no_punct = ""
for char in my_str:
    if char not in punctuations:
        no_punct = no_punct + char

# display the unpunctuated string
print(no_punct)











