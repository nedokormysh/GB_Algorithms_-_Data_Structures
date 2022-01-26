import random

# matrix = [[random.randint(1, 10) for _ in range(5)] for _ in range(7)]
#
# # for line in matrix:
# #     print(line)
#
# for line in matrix:
#     for item in line:
#         print(f'{item:>4}', end='')
#     print()
#
# print(len(matrix))
#
# # Sum of elements in lines and columns
#
# sum_colum = [0] * len(matrix[0])
# # print(sum_colum)
#
#
# for line in matrix:
#     sum_line = 0
#
#     for i, item in enumerate(line): #в i будет лежать номер столбца
#         sum_line += item
#         sum_colum[i] += item
#
#         print(f'{item:>5}', end='')
#     print(f'   |{sum_line}')
#
# print('-' * len(matrix) * 5)
#
# for s in sum_colum:
#     print(f'{s:>5}', end='')

# exchange of values main and not main diagonals in square matrix
#var 1
# size = 3
#
# matrix = [[random.randint(1, 10) for _ in range(size)] for _ in range(size)]
#
# for line in matrix:
#     for item in line:
#         print(f'{item:>4}', end='')
#     print()
#
# for i in range(size):
#     for j in range(size):
#         if i == j:
#             spam = matrix[i][j]
#             matrix[i][j] = matrix[i][size - 1 - j]
#             matrix[i][size - 1 - j] = spam
#
# print('*' * 30)
#
# for line in matrix:
#     for item in line:
#         print(f'{item:>4}', end='')
#     print()

# var2

size = 3

matrix = [[random.randint(1, 10) for _ in range(size)] for _ in range(size)]

for line in matrix:
    for item in line:
        print(f'{item:>4}', end='')
    print()

# for i, lines in enumerate(matrix):
#     lines[i], lines[-i-1] = lines[-i-1], lines[i]

for i in range(size):
    matrix[i][i], matrix[i][-i-1] = matrix[i][-i-1], matrix[i][i]

print('*' * 30)

for line in matrix:
    for item in line:
        print(f'{item:>4}', end='')
    print()