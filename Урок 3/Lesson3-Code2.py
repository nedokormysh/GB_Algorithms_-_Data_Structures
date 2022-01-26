import random


def binary_search(array, value):
    left = 0
    right = len(array) - 1
    pos = len(array) // 2

    while array[pos] != value and left <= right:
        if value > array[pos]:
            left = pos + 1
        else:
            right = pos - 1

        pos = (left + right) // 2

    # if left > right:
    #     return -1
    # else:
    #     return pos

    return -1 if left > right else pos


a = [random.randint(0, 1000) for _ in range(100)]
a.sort()
print(a)

n = int(input('Введите число для поиска: '))

print(binary_search(a, n))
