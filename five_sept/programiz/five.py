
# Find the factores of the number

# this function computes the factor of the argument passed
def print_factors(x):
    print('the factors of', x, 'are:')
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)

num= 320

print_factors(num)