def fibonacci(n):
    """Return the nth number of the fibonacci series"""
    previous = 0
    current = 1
    next = 0
    if n == 1:
        return 0
    elif n == 2:
        return 1
    if n > 2:
        for number in range(n-2):
            next = previous + current
            previous = current
            current = next
    return current


def lucas(n):
    """Return the nth number of the lucas series"""
    previous = 2
    current = 1
    next = 0
    if n == 1:
        return 2
    elif n == 2:
        return 1
    if n > 2:
        for number in range(n-2):
            next = previous + current
            previous = current
            current = next
    return current


def sum_series(n, previous=0, current=1):
    """Return the nth number of a series where each integer is the sum of the previous two"""
    next = 0
    if n == 1:
        return previous
    elif n == 2:
        return current
    if n > 2:
        for number in range(n-2):
            next = previous + current
            previous = current
            current = next
    return current
