import sys
import ctypes
import struct


a = 5
aa = 59
x = y = aa
b = 125.54
c = 'Hello World!'

print(id(a)) #адрес объекта в памяти по которому лежит объект целого типа
print(sys.getsizeof(a))

print(ctypes.string_at(id(a), sys.getsizeof(a))) # метод возвращает строку из байт
print(struct.unpack('LLLLLLl', ctypes.string_at(id(a), sys.getsizeof(a)))) # стракт помогает расшифровать бинарную строку ctypes
print(id(int))

# (34, 0, 2187235280, 32765, 1, 0, 5)
#  34 - счётчик ссылок. длинное число - указатель на тип объекта. последняя 5 - значение самого объекта

print(ctypes.string_at(id(aa), sys.getsizeof(aa))) # метод возвращает строку из байт
print(struct.unpack('LLLLLLl', ctypes.string_at(id(aa), sys.getsizeof(aa)))) # стракт помогает расшифровать бинарную строку ctypes
print(id(int))


print('*' * 50)
print(id(b))

print(ctypes.string_at(id(b), sys.getsizeof(b)))
print(struct.unpack('LLLd', ctypes.string_at(id(b), sys.getsizeof(b))))

# (3, 0, 2187228624, 125.54)
# 3 за счёт вызова функций анпак и стрингэт
z = b
b = 122.99 # целые и вещ.числа - неизменяемые. поэтому при создании нового числа по сути создаём новый объект
# z ссылается на старый объект
print(ctypes.string_at(id(b), sys.getsizeof(b)))
print(struct.unpack('LLLd', ctypes.string_at(id(b), sys.getsizeof(b))))
print(id(float))
# адрес на который ссылается объект и адрес флоат - один и тот же


print('*' * 50)
print(id(c))

print(ctypes.string_at(id(c), sys.getsizeof(c)))
print(struct.unpack('LLLLLLLLLLli' + 'c' * 13, ctypes.string_at(id(c), sys.getsizeof(c))))
# 13 букв с. HelloWorld содержит 12 символов в качестве 13 конец строки - возврат каретки
# (3, 0, 2187247936, 32765, 12, 0, 1122370879, 3277570802, 720424164, 580, 0, 0, b'H', b'e', b'l', b'l', b'o', b' ', b'W', b'o', b'r', b'l', b'd', b'!', b'\x00')
# 3 - число ссылок, 2187247936 - указатель на тип объекта, в конце символы в виде байт-строк: один байт- один символ

print('*' * 50)
print('lst')

def show_sizeof(x, level=0):
    print("\t" * level, x.__class__, sys.getsizeof(x), x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_sizeof(xx, level + 1)
        else:
            for xx in x:
                show_sizeof(xx, level + 1)

lst = [1]
show_sizeof(lst)
# print(struct.unpack('LLLL' + 'L' * 5 * 4, ctypes.string_at(id(lst), sys.getsizeof(lst))))
print(struct.unpack('L' + 'L' * 5 * 3, ctypes.string_at(id(lst), sys.getsizeof(lst))))

# 4 L - служебная инфа, где хранится счётчик ссылок, указатель на тип объекта. для хранения адреса каждого объекта используется 5 букв L. т.к. у нас 4 объекта

lst1 = [1, 2, 3, 4]
show_sizeof(lst1)
# print(struct.unpack('LLLL' + 'L' * 5 * 4, ctypes.string_at(id(lst), sys.getsizeof(lst))))
print(struct.unpack('L' * 5 * 3 * 2, ctypes.string_at(id(lst1), sys.getsizeof(lst1))))

# # 4 L - служебная инфа, где хранится счётчик ссылок, указатель на тип объекта. для хранения адреса каждого объекта используется 5 букв L. т.к. у нас 4 объекта
# у меня так не получилось. Мой лист занимает 120 байт. Поэтому выделил просто 'L' * 5 * 3 * 2 (4 * 5 * 3 * 2). Не знаю насколько это верно, но хотя бы работает.




