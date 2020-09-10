# wap to calculate the area of triangle

# if a,b and c are three sides of a triangle then
# s=(a+b+c)/2
# area= sqrt(s(s-a)*(s-b)*(s-c))

a=5
b=5
c=5

# Take input from user
# a= float(input('enter first side: '))
# b= float(input('enter second side: '))
# c= float(input('enter third side: '))


s= (a+b+c)/2

area= (s*(s-a)*(s-b)*(s-c))**0.5

print('the area of the triangle is %0.2f' %area)


