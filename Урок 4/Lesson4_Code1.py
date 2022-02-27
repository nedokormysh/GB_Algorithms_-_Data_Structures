import timeit

z = 2 + 2
# print(z)
print(timeit.timeit('z = 2 + 2'))
print(timeit.timeit('x = sum(range(10))'))