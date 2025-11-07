def power(x, n):
    if n == 0:
        return 1
    elif n > 0:
        return x * power(x, n - 1)
    else:  # обработка отрицательной степени
        return 1 / power(x, -n)

print(power(2, 5))   # 32
print(power(3, 0))   # 1
print(power(2, -3))  # 0.125
print(power(5, 1))   # 5
