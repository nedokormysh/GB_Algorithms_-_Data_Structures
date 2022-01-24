def func(a, b):
    if a == b:
        return f'{a}'
    elif a > b:
        return f'{a}, {func(a - 1, b)}'
    elif a < b:
        return f'{a}, {func(a + 1, b)}'

print(func(12, 10))
