# checking amrstrong number

# a no. is armstrong no. of order of n if
# abcd = a(raise n) + b(raise n) + c(raise n) + ......

# example of number of 3 digits, the sum of cubes of each digit is equal to the number itself.
# 153 = 1*1*1 + 5*5*5 + 3*3*3 = 3 + 125 + 27 = 153

# user input
num= int(input('enter a number: '))

# initialize sum
sum= 0

# find the sum of the cube of each digit
temp= num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

# display the result
if num == sum:
    print(num, 'is an armstrong number')
else:
    print(num, 'is not an armstrong number')