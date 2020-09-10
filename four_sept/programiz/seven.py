# swap 2 variables

# Non Pythonic way

# x= 5
# y= 10

# to take inputs from the user
# x = input('enter value of x: ')
# y= input('enter value of y: ')

# create a temporary variable and swap the values
# temp= x
# x= y
# y = temp
#
# print('the value of x after swapping: {}'.format(x))
# print('the value of y after swapping: {}'.format(y))




# Pythonic way to do

x= 5
y= 4

x,y = y,x
print('x=',x)
print('y=',y)