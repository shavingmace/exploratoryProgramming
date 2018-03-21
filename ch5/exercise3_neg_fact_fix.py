def factorial_fixed(n):
    if n == 1 or 0:
        return 1
    elif n < 0:
        return None
    else:
        return factorial_fixed(n-1) * n

print(factorial_fixed(-3))
print(factorial_fixed(5))
