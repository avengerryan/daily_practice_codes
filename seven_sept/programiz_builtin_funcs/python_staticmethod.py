
# python staticmethod
# transforms a method into a static method


# create a static method using staticmethod()

class Mathematics:

    def addNumbers(x, y):
        return x + y

# create addNumbers static method
Mathematics.addNumbers = staticmethod(Mathematics.addNumbers)

print('the sum is: ', Mathematics.addNumbers(5, 10))
























