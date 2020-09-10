# Display powers of 2 using anonymous function

# using anonymous lambda function inside the built in function map() to find powers of 2

terms= 10

# user input
# terms= int(input('how many terms? '))

# use anonymous function
result= list(map(lambda x:
                 2**x,
                 range(terms)))

print('The total terms are:', terms)
for i in range(terms):
    print('2 raised to power', i, 'is', result[i])