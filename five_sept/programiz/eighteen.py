
# check whether a string is palindrome or not

# A palindrome is a string that is the same read forward or backward

# example: 'dad' is the same in forward or reverse direction.
# e.g. 'aibohphobia' - meaning irritable fear of palindrome



# checking if a string is palindrome or not

# my_str = 'aIbohPhoBiA'
my_str = 'RajeshAWankhade'


# make it suitable for caseless comparison
my_str = my_str.casefold()

# reverse the string
rev_str = reversed(my_str)

# check if the string is equal to its reverse
if list(my_str) == list(rev_str):
    print('the string is a palindrome.')
else:
    print('the string is not a palindrome.')















