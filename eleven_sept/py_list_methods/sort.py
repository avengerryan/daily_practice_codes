
# python list sort() : sorts elements of a list
# The sort() method sorts the elements of a given list in a specific ascending
# or descending order.

# list.sort(key=..., reverse=...)


# sorted(list, key=..., reverse=...)



"""

# e.g.1: sort a given list

# vowels list
vowels = ['e', 'a', 'u', 'o', 'i']

# sort the vowels
vowels.sort()

# print vowels
print('Sorted List: ', vowels)

"""




"""

# e.g. 2: sort the list in descending order.

# vowels list
vowels = ['e', 'a', 'u', 'o', 'i']

# sort the vowels
vowels.sort(reverse=True)

# print vowels
print('Sorted list(in descending):', vowels)

"""




"""

# sort with custom function using key

# list.sort(key=len)

# sorted(list, key=len)

# e.g. 3: sort the list using key

# take second element for sort

def takeSecond(elem):
    return elem[1]

# random list
random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# sort list with key
random.sort(key=takeSecond)

print('Sorted list:', random)

"""







# sorting using custom key

employees = [
    {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
    {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
    {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
    {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
    ]


# custom functions to get employee info
def get_name(employee):
    return employee.get('Name')

def get_age(employee):
    return employee.get('age')

def get_salary(employee):
    return employee.get('salary')

# sort by name (Ascending order)
employees.sort(key=get_name)
print(employees, end='\n\n')

# sort by age (ascending order)
employees.sort(key=get_age)
print(employees, end='\n\n')

# sort by salary (descending order)
employees.sort(key=get_salary, reverse=True)
print(employees, end='\n\n')




























