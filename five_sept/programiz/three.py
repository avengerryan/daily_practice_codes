
# finding LCM

# the LCM of 2 nos. is the smallest positive integer that is perfectly divisible by the 2 given nos.

# example: the LCM of 12 and 14 is 84

def compute_lcm(x, y):
    # choose the greater number
    if x > y:
        greater = x
    else:
        greater = y
    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm

num1= 54
num2= 24

print('The LCM is', compute_lcm(num1, num2))