
# Python eval()
# runs python code within program

# how eval() works in Python


"""
x = 1
print(eval('x + 1'))
"""


# Example: practical example to demonstrate use of eval()


# perimeter of square
def calculatePerimeter(l):
    return 4*l

# Area of square
def calculateArea(l):
    return l*l

expression = input("Type a function: ")

for l in range(1, 5):
    if (expression == 'calculatePerimeter(l)'):
        print('if length is ', l, ", Perimeter = ", eval(expression))
    elif (expression == 'calculateArea(l)'):
        print('if length is ', l, ', Area = ', eval(expression))
    else:
        print('wrong Function')
        break

















