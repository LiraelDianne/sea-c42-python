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
