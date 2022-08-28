def fib_rec(n):
    if n < 0:
        raise ValueError("n must be greater than zero")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib_rec(n-1) + fib_rec(n-2)


fib_array = [0, 1]


def fib_rec_memo(n):
    if n < 0:
        raise ValueError("n must be greater than zero")
    elif n < len(fib_array):
        return fib_array[n]
    else:
        fib_array.append(fib_rec_memo(n - 1) + fib_rec_memo(n - 2))
        return fib_array[n]


def fib_iter(n):
    a = 0
    b = 1
    if n < 0:
        raise ValueError("n must be greater than zero")
    elif n == 0:
        return 0
    elif n == 1:
        return b
    else:
        for _ in range(1, n):
            c = a + b
            a = b
            b = c
        return b
