
# Python isinstance() : checks if a object is an instance of class


"""
# example 1: how isinstance() works

class Foo:
    a = 5

fooInstance = Foo()

print(isinstance(fooInstance, Foo))
print(isinstance(fooInstance, (list, tuple)))
print(isinstance(fooInstance, (list, tuple, Foo)))


"""




# example 2: working of isintance() with native types

nums = [1, 2, 3]

result = isinstance(nums, list)
print(nums, 'instance of list?', result)

result = isinstance(nums, dict)
print(nums, 'instance of dict?', result)

result = isinstance(nums, (dict, list))
print(nums, 'instance of dict or list?', result)


number = 5

result = isinstance(number, list)
print(number,'instance of list?', result)

result = isinstance(number, int)
print(number,'instance of int?', result)







