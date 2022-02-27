import cProfile

def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')

def fib_loop(n):
    if n < 2:
        return n

    first, second = 0, 1

    for i in range(0, n - 1):
        first, second = second, first + second

    return second

# test_fib(fib_loop)

# "Lesson4_Code6.fib_loop(10)"
# 1000 loops, best of 5: 1.87 usec per loop


#  "Lesson4_Code6.fib_loop(100)"
# 1000 loops, best of 5: 5.51 usec per loop


# "Lesson4_Code6.fib_loop(500)"
# 1000 loops, best of 5: 44.8 usec per loop


cProfile.run('fib_loop(1000)')

# 4 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Lesson4_Code6.py:10(fib_loop)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}