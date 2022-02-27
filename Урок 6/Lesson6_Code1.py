print(id(100)) # по ккакому адресу в памяти хранится целое число 100. целые числа -5 до 255, тру, фалсе и нон - стат информация
# до окончания программы

a = 111 - 11

print(id(a))
print(id(1000))

b = 1020 - 20

print(id(b))

print(id(100000))

c = 100020 - 20

print(id(c))


stack = []
stack.append(1)
stack.append(2)
print(stack.pop())

spam = stack.pop()
print(stack)
stack.append(spam)
print(stack)