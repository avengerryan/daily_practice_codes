
# python iter(): returns an iterator

# the python iter() function returns an iterator for the given object


"""

# example 1: working of python iter()

# list of vowels
vowels = ['a', 'e', 'i', 'o', 'u']
vowels_iter = iter(vowels)

print(next(vowels_iter))
print(next(vowels_iter))
print(next(vowels_iter))
print(next(vowels_iter))
print(next(vowels_iter))

"""


"""
# example 2: iter() for custom objects

class PrintNumber:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if(self.num >= self.max):
            raise StopIteration
        self.num += 1
        return self.num

print_num = PrintNumber(3)

print_num_iter = iter(print_num)
print(next(print_num_iter))
print(next(print_num_iter))
print(next(print_num_iter))

# raises StopIteration
print(next(print_num_iter))

"""


# example 3: iter() with sentinel parameter

# with open('mydata.txt') as fp:
#     for line in iter(fp.readline, ''):
#         processLine(line)


















