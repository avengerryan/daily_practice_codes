# convert celsius to fahrenheit

# celsius * 1.8 = fahrenheit - 32

# Python program to convert temperature in celsius to fahrenheit

# change this value for a different result
# celsius= 37.5

# user input
celsius_temper= float(input('enter the temperature value: '))

# calculate fahrenheit
# fahrenheit= (celsius*1.8)+32
fahrenheit= (celsius_temper * 1.8)+32

print('%0.1f degree celsius is equal to %0.1f degree fahrenheit' %(celsius_temper, fahrenheit))