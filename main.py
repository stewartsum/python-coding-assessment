def factorial(n):
    if n < 0:
        raise ValueError("n cannot be negative")
    if n == 0:
        return 1
    return n * factorial(n - 1)
