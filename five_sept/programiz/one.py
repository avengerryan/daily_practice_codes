
# find HCF or GCD

# to find GCD or HCF of 2 nos. using 2 different methods, we use function and loops and Euclidean algorithm

# the HCF or GCD of 2 nos. is the largest positive integer that perfectly divides the 2 given nos
# example: HCF of 12 and 14 is 2


# define a function
def compute_hcf(x, y):

    # choose the smaller no
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf

# num1= 54
# num2= 24

print('The HCF is', compute_hcf(54, 24))
# print('The HCF is', compute_hcf(x= 16, y= 27))
# print('The HCF is', compute_hcf(num1, num2))