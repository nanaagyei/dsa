# Implementing the fibonacci sequence using memoization method in dynamic programming

from tempfile import tempdir


def fib(n, memo={}):
    if n == 0 or n == 1:
        return n
    
    if not memo.get(n):
        memo[n] = fib(n-2) + fib(n-1)
    
    return memo[n]

# Bottom-up approach of fibonacci
# makes use of a temp variable

def fibonacci(n):
    if n == 0:
        return 0
    
    a = 0
    b = 1

    for i in range(1, n):

        temp = a
        a = b
        b = temp + a
    
    return b