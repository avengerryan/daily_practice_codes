
# sort words in alphabetic order


# we will be using loop. we will be sorting lexicographically.


my_str = "Hello this Is an Example With cased letters"


# to take input from the user
# my_str = input("enter a string: ")

# breakdown the string into a list of words
words =  my_str.split()

# sort the list
words.sort()

# display the sorted words

print('the sorted words are: ')
for word in words:
    print(word)


# using split() method the string is converted into a list of words.
# the split() method splits the string at whitespaces

# the list of words is then sorted using the sort() method, and all the words are displayed
















