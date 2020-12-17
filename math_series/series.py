def fibonacci(n: int) -> int:
    """ Calculates and returns the nth number fo the fibonacci series"""
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n: int) -> int:
    """ Calculates and returns the nth number fo the lucas series"""
    if n == 0:
        return 2
    if n == 1:
        return 1
    return lucas(n - 1) + lucas(n - 2)


def sum_series(n: int, a=0, b=1) -> int:
    """ Calculates and returns the nth number of various summation series series"""
    if n == 0:
        return a
    if n == 1:
        return b
    return sum_series(n - 1, a, b) + sum_series(n - 2, a, b)
