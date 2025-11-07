def power(x, n):
    if n == 0:
        return 1
    elif n > 0:
        return x * power(x, n - 1)
    else:  # обработка отрицательной степени
        return 1 / power(x, -n)

