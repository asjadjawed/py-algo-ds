def factorial(n):
    if n is None:
        return None

    if n <= 1:
        return n
    else:
        return n * factorial(n-1)
