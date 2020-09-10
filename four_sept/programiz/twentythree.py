# find the sum of natural numbers

num= 16

if num < 0:
    print('enter a positive number')
else:
    sum = 0
    # use while loop to iterate until zero
    while(num > 0):
        sum += num
        num -= 1
    print('the sum is', sum)