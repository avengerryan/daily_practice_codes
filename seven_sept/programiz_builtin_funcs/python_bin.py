
# Python bin()


# the bin() method converts and returns the binary equivalent of a given integer.
# if the parameter isn't an integer, it has to implement __index__() method to return an integer.



number = 5
print('the binary equivalent of 5 is:', bin(number))


print(30*'=')


# convert an object to binary implementing __index__() method

class Quantity:
    apple = 1
    orange = 2
    grapes = 2

    def __index__(self):
        return self.apple + self.orange + self.grapes


first = Quantity()

# print('the binary equivalent of quantity is: ', bin(Quantity()))
print('the binary equivalent of quantity is: ', bin(first))


