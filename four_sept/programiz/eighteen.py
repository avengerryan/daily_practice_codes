# find the factorial of a number

# the factorial of a number is the product of all the integers from 1 to that number.

# example: the factorial of 6 is 1*2*3*4*5*6 = 720

# change the value for a different result

num= 7

# user input
# num= int(input('Enter a number: '))

factorial= 1

# check if the number is negative, positive or zero

if num < 0:
    print('sorry, factorial does not exist for negative numbers')
elif num == 0:
    print('the factorial of 0 is 1')
else:
    for i in range(1, num + 1):
        factorial = factorial*i
    print('the factorial of', num, 'is', factorial)








  