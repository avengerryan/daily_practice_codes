
# python string format_map() : formats the string using dictionary
# the format_map() method is similar to str.format(**mapping) except that
# str.format(**mapping) created a new dictionary whereas str.format_map(mapping)
# doesn't

# str.format(mapping)







"""

point = {'x': 4, 'y': -5}
print('{x} {y}'.format(**point))

"""





"""

# e.g.1: how format_map() works

point = {'x': 4, 'y': -5}
print('{x} {y}'.format_map(point))

point = {'x':4, 'y':-5, 'z':0}
print('{x} {y} {z}'.format_map(point))

"""








# e.g.2: how format_map() works with dict subclass

class Coordintate(dict):

    def __missing__(self, key):
        return key

print('({x}, {y})'.format_map(Coordintate(x='6')))
print('({x}, {y})'.format_map(Coordintate(y='5')))
print('({x}, {y})'.format_map(Coordintate(x='6', y='5')))
















































