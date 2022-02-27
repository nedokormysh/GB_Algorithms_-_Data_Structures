import cProfile
import functools

def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')


@functools.lru_cache()
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

# test_fib(fib)
# print(fib(10))
#  "Lesson4_Code7.fib(10)"
# 1000 loops, best of 5: 82.4 nsec per loop

#  "Lesson4_Code7.fib(100)"
# 1000 loops, best of 5: 88.2 nsec per loop

# "Lesson4_Code7.fib(150)"
# 1000 loops, best of 5: 84.7 nsec per loop


# cProfile.run('fib(100)')

# 14 function calls (4 primitive calls) in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      11/1    0.000    0.000    0.000    0.000 Lesson4_Code7.py:12(fib)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# 100
# 104 function calls (4 primitive calls) in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#     101/1    0.000    0.000    0.000    0.000 Lesson4_Code7.py:12(fib)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



# cProfile.run('fib(200)')

# 204 function calls (4 primitive calls) in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#     201/1    0.001    0.000    0.001    0.001 Lesson4_Code7.py:12(fib)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}