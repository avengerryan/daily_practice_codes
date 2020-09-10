
# fibonacci sequence using recursion

# example: 0,1,1,2,3,5,8

def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))

nterms= 10

# check if the no. if terms is valid
if nterms <= 0:
    print('please enter a positive integer')
else:
    print('Fibonacci sequence:')
    for i in range(nterms):
        print(recur_fibo(i))