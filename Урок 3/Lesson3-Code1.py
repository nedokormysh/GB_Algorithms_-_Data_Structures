# Удаление элемента во время его итерирования

# list1 = [1, 2, 3, 4]
# list2 = [1, 2, 3, 4]
# list3 = [1, 2, 3, 4]
# list4 = [1, 2, 3, 4]
#
# for i, item in enumerate(list1):
#     del item
#     # print(item)
#
# print(list1)
#
#
# for i, item in enumerate(list2):
#     list2.remove(item)
#
# print(list2)
#
# for i, item in enumerate(list3):
#     list3.pop(i)
#
# print(list3)
#
#
# # удаление по списку, а цикл по его срезу
# for i, item in enumerate(list4[:]):
#     list4.remove(item)
#
# print(list4)

# Крестики нолики, где Икс побеждает с первой попытки
# row = [''] * 3
# print(row)
# board = [row] * 3
# print(board)
# board[0][0] = 'X'
# print(board)
#
# board = [''] * 9
# print(board)
#
# board = [[''] * 3 for _ in range(3)]
# print(board)
# board[0][0] = 'X'
# print(board)

# Те же операнды, но другая история?

# a = [1, 2, 3, 4]
# b = a
# a = a + [5, 6, 7]
# print(a, b)
#
# a = [1, 2, 3, 4]
# b = a
# a += [5, 6, 7]
# print(a, b)

# Игла в стоге сена

# t = ('one', 'two')
#
# for i in t:
#     print(i)
#
# t = ('one')
#
# for i in t:
#     print(i)
#
# t = ('one',)
#
# for i in t:
#     print(i)

# Сохраним только уникальные значения

# lst = [1, 2, 3, 6, 1, 2, 3, 6]
# print(list(set(lst)))

# Ключ словаря - изменяемый объект

set_x = {1, 2, 3}
lst_x = {1, 4, 9}

# dict_x = {set_x: lst_x}

dict_x = {frozenset(set_x): lst_x}
dict_y = {tuple(lst_x): set_x}