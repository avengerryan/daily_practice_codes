
# finding factorial no using recursion

# factorial of a no. is the product of all the integers from 1 to that no.

# example: the factorial of 6 is 1*2*3*4*5*5 = 720
# factorial is not defined for negative nos. and the factorial of zero is one, 0! = 1


def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n*recur_factorial(n-1)


num = 7
if num < 0:
    print('Sorry, factorial does not exist for negative nos.')
elif num == 0:
    print('the factorial of 0 is 1')
else:
    print('the factorial of', num, 'is', recur_factorial(num))




