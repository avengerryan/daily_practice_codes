
# Python reversed() : returns the reversed iterator of a sequence
# the reversed() function returns the reversed iterator of the given sequence


# reversed(seq)


"""

# e.g. 1: using reversed() in string, tuple, list and range

# for string
seq_string = 'Python'
# print(reversed(seq_string))
print("reversed string:", list(reversed(seq_string)))

# for tuple
seq_tuple = ('P', 'y', 't', 'h', 'o', 'n')
print("reversed tuple:", list(reversed(seq_tuple)))

# for range
seq_range = range(5, 9)
print("reversed range:", list(reversed(seq_range)))


# for list
seq_list = [1, 2, 4, 3, 5]
print("reversed list:", list(reversed(seq_list)))

"""


# e.g. 2: reversed() in custom objects

class Vowels:
    vowels = ['a', 'e', 'i', 'o', 'u']

    def __reversed__(self):
        return reversed(self.vowels)

v = Vowels()

print(list(reversed(v)))
# print(list(reversed(Vowels())))




















