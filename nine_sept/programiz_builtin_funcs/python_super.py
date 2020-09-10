
# Python super() : returns a proxy object of the base class
# the super() builtin returns a proxy object (temporary object of the superclass)
# that allows us to access methods of the base class.


"""

# e.g. 1: super() with single inheritance

class Mammal(object):
    def __init__(self, mammalName):
        print(mammalName, 'is a warm-blooded animal.')

class Dog(Mammal):
    def __init__(self):
        print('Dog has four legs')
        super().__init__('Dog')


d1 = Dog()

"""


"""

# we can also change name of the base class by using super()

class Mammal(object):
    def __init__(self, mammalName):
        print(mammalName, 'is a warm-blooded animal.')



class Dog(CanidaeFamily):
    def __init__(self):
        print('Dog has four legs.')

        # no need to change this
        super().__init__('Dog')

"""





# e.g. 2: super() with multiple inheritance


class Animal:
    def __init__(self, Animal):
        print(Animal, 'is an animal.')

class Mammal(Animal):
    def __init__(self, mammalName):
        print(mammalName, 'is a warm-blooded animal.')
        super().__init__(mammalName)

class NonWingedMammal(Mammal):
    def __init__(self, NonWingedMammal):
        print(NonWingedMammal, "can't fly.")
        super().__init__(NonWingedMammal)

class NonMarineMammal(Mammal):
    def __init__(self, NonMarineMammal):
        print(NonMarineMammal, "can't swim.")
        super().__init__(NonMarineMammal)

class Dog(NonMarineMammal, NonWingedMammal):
    def __init__(self):
        print('Dog has 4 legs,')
        super().__init__('Dog')

d = Dog()
print('')
bat = NonMarineMammal('Bat')





























