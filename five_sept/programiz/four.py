
# finding LCM using GCD

# the product of 2 nos. is equal to the product of the least common multiple and greatest common divisor of those 2 nos.

# number1 * number2 = LCM * GCD

# this function computes GCD
def compute_gcd(x, y):

    while(y):
        x, y = y, x % y
    return x

# this function mcomputes LCM
def compute_lcm(x, y):

    lcm = (x*y)//compute_gcd(x, y)
    return lcm

num1= 54
num2= 24

print('The LCM is', compute_lcm(num1, num2))