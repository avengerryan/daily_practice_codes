# Check if a number is odd or even

# a number is even if division by 2 gives a remainder of 0
# if the remainder is 1, it is an odd number

num= int(input('enter a number: '))

if (num % 2) == 0:
    print('{0} is even'.format(num))
else:
    print('{0} is odd'.format(num))