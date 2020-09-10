
# sum of natural nos. using recursion

# using a recursive function recur_sum() to compute the sum up to the given no.


def recur_sum(n):

    if n <= 1:
        return n
    else:
        return n + recur_sum(n-1)


num = 16

if num < 0:
    print('enter a positive no.')
else:
    print('the sum is', recur_sum(num))