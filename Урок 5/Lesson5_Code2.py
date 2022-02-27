from collections import deque

a = deque()
b = deque('abcdef')
c = deque([1, 2, 3, 4])

print(a, b, c, sep='\n')

b = deque('abcdef', maxlen=3)
c = deque([1, 2, 3, 4], maxlen=4)

print(b, c, sep='\n')

c.clear()
print(c)


print('*' * 100)
d = deque([i for i in range(6)])
print(d)
d.append(5)
print(d)
d.appendleft(6)
print(d)

d.extend([7, 8, 9])
print(d)
d.extendleft([10, 11, 12])
print(d)

print('*' * 100)

d = deque([i for i in range(6)], maxlen=7)
print(d)
d.append(5)
print(d)
d.appendleft(6)
print(d)

d.extend([7, 8, 9])
print(d)
d.extendleft([10, 11, 12])
print(d)

print('*' * 100)
f = deque([i for i in range(5)], maxlen=7)
print(f)
x = f.pop()
y = f.popleft()

print(f, x, y, sep='\n')

print('*' * 100)
g = deque([i for  i in range(5)], maxlen=7)
print(g.count(2))
print(g.index(3))
print(g)
g.insert(2, 6)
print(g)

print('*' * 100)
h = deque([i for i in range(5)], maxlen=7)
print(h)
h.reverse()
print(h)

h.rotate(3)
print(h)


print('*' * 100)

import random

array = [random.randint(-100, 100) for _ in range (10)]
print(array)

deq = deque()

for item in array:
    if item >= 0:
        deq.append(item)
    else:
        deq.appendleft(item)

print(deq)

print('*' * 100)


with open ('log.txt', 'r',encoding='utf-8') as f:
    last_ten = deque(f, 10)

print(last_ten)