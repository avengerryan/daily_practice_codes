# Find the largest among the three numbers

# change the values of num1, num2, and num3

num1= 10
num2= 14
num3= 12

# user input
# num1= float(input('enter first number: '))
# num2= float(input('enter second number: '))
# num3= float(input('enter third number: '))

if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3
print('the largest number is', largest)