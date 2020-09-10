
# finding HCF or GCD using euclidean algorithm

# function to find HCF by using Euclidean algorithm

def compute_hcf(x, y):
    while(y):
        x, y = y, x % y
    return x

hcf= compute_hcf(300, 400)
print('The HCF is', hcf)