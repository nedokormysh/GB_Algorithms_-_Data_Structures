import random


# # Deviding massive for plus and minus massive
# plus = []
# minus = []
#
# array = [random.randint(-100, 100) for _ in range(30)]
# print(array)
#
# for i in array:
#     if i > 0:
#         plus.append(i)
#     else:
#         minus.append(i)
#
# print(plus)
# print(minus)
#
# arr_below = [item for item in array if item < 0]
# arr_larger = [item for item in array if item > 0]
#
# print(arr_below)
# print(arr_larger)

# Entring element to massive in random position of massive
# var1
# array = [random.randint(-100, 100) for _ in range(10)]
# print(array)
#
# n = int(input('Which number do you want to insert: '))
# p = int(input('There do you want to insert your number: '))
#
# array.append(None)
#
# i = len(array) - 1 #перемеррая для элементов, которые хотим поменять. Изначально указываем на последний
#
# while i > p:
#     array[i - 1], array[i] = array[i], array[i - 1]
#     i -= 1
#
# array[p] = n
#
# print(array)

# var2

# array = [random.randint(-100, 100) for _ in range(10)]
# print(array)
#
# n = int(input('Which number do you want to insert: '))
# p = int(input('There do you want to insert your number: '))
#
# array.insert(p, n)
#
# print(array)

# var3
array = [random.randint(-100, 100) for _ in range(10)]
print(array)

n = int(input('Which number do you want to insert: '))
p = int(input('There do you want to insert your number: '))
# forming new massive, so two more memory used
array_new = array[:p] + [n] + array[p:]

print(array_new)
