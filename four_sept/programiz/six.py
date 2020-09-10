# solve quadratic equation

import cmath

# a= 1
# b= 2
# c= 3

# user input
a= int(input("enter 1st number: "))
b= int(input('enter 2nd number: '))
c= int(input('enter 3rd number: '))

d= (b**2) - (4*a*c)

sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2= (-b+cmath.sqrt(d))/(2*a)

print('the solution are {0} and {1}'.format(sol1, sol2))
