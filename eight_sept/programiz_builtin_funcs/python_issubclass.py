
# Python issubclass() : checks if a class is subclass of another class

# the issubclass() function checks if the class argument is a sublcass (first argument) of classinfo (second argument) class.


# example: how issubclass() works


class Polygon:
    def __init__(polygonType):
        print('Polygon is a ', polygonType)

class Triangle(Polygon):
    def __init__(self):

        Polygon.__init__('triangle')

print(issubclass(Triangle, Polygon))
print(issubclass(Triangle, list))
print(issubclass(Triangle, (list, Polygon)))
print(issubclass(Polygon, (list, Polygon)))


















