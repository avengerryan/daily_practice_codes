# checking prime number

# Prime number is a positive interger greater than 1 which has no other factores except 1 and the number itself.


num = 407

# to take input from the user
# num = int(input('enter a number: '))

# prime numbers are greater than 1
if num > 1:
    # check factors
    for i in range(2, num):
        if (num % i) == 0:
            print(num, 'is not a prime number')
            print(i, 'times', num//i, 'is', num)
            break
    # else used with for loop
    else:
        print(num, 'is a prime number')

else:
    print(num, 'is not a prime number')

