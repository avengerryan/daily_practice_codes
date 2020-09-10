
# python open() : returns a file object.
# the open() function opens the file (if possible) and returns the corresponding file object



"""

# opens test.text file of the current directory
f = open('test.txt')

# specifying the full path
f = open("C:/Python22/README.txt")

"""



"""

# example 2: providing mode to open()

# opens the file in reading mode
f = open("path_to_file", mode='r')

# opens the file in writing mode
f = open("path_to_file", mode='w')

# opens for writing to the end
f = open("path_to_file", mode='a')

"""




# Python's default encoding is ASCII. You can easily change it by a passing the encoding parameter

f = open("path_to_file", mode='r', encoding='utf-8')