lst = []

lst.append(1)
lst.extend([2, 3, 4])

print(lst)

lst.insert(1, 5)

print(lst)

# количество зарезервированной памяти
# allocated = 0
# ньюсайз - текущий размер списка. Будем увеличивать от нуля до 99
# for newsize in range(100):
# если количество зарезервированной памяти не хватает для добавления очередного элемента
#     if allocated < newsize:
#         старое значение ньюсайз со сдвигом на 3 байта вправо т.е. последние три байта мы забываем + 3 если ньюсайз меньше 9
#         new_allocated = (newsize >> 3) + (3 if newsize < 9 else 6)
#         allocated = newsize + new_allocated
#
#     print(newsize, allocated)

last = lst.pop()

print(lst, last)

last = lst.pop()

print(lst, last)

lst.remove(5)
print(lst)