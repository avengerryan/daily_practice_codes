
# convert decimal to binary using recursion


def convert_to_binary(n):
    if n > 1:
        convert_to_binary(n//2)
    print(n % 2, end='')


# decimal no
dec = 27

convert_to_binary(dec)
print()