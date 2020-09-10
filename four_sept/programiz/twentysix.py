# convert decimal to  binary, octal and hexadecimal

# decimal system is base 10(ten symbols, 0-9, are used to represent a no)
# similarly,
# Binary is base 2,
# octal is base 8
# hexadecimal is base 16

# A no. with prefix 0b is binary, 0o is octal, 0x is hexadecimal

# 60 (decimal) = 0b11100 (binary) = 0o74 (octal) = 0x3c (hexadecimal)

dec= 344

print('the decimal value of', dec, 'is:')

# we used built in functions bin(), oct() and hex() to convert the decimal into respective no
print(bin(dec), 'in binary.')
print(oct(dec), 'in octal')
print(hex(dec), 'in hexadecimal.')