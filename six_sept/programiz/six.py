
# Finding the hash of a file

# Hash functions take an arbitrary amount of data and return
# a fixed length bit string. The o/p of the function is called the digest message

# Hash functions are widely used in cryptography for authentication purposed.
# there are many hashing functions like MD5, SHA-1 etc.



# importing the hashlib module
import hashlib


def hash_file(filename):
    """This function returns the SHA-1 hash of the file passed into it"""

    # make a hash object
    h = hashlib.sha1()

    # open file for reading in binary mode
    with open(filename, 'rb') as file:

        # loop till the end of the file
        chunk = 0
        while chunk != b'':
            # read only 1024 bytes at a time
            chunk = file.read(1024)
            h.update(chunk)

    # return the hex representation of digest
    return h.hexdigest()


message = hash_file("track1.mp3")
print(message)























