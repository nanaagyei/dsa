def fib(n):
    """
    Calculate Fibonacci number
    :param n:
    :return: Fibonacci number at nth position
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
