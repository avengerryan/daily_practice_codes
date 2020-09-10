
# Python filter()
# constructs iterator from elements which are true

# filter(function, iterable)

# How filter() works for iterable list

# list of letters
letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

# function that filters vowels
def filterVowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    if(letter in vowels):
        return True
    else:
        return False

filteredVowels = filter(filterVowels, letters)

print('The filtered vowels are: ')
for vowel in filteredVowels:
    print(vowel)



















